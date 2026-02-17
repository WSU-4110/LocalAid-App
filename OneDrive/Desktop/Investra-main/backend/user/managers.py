from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    
    # we will take BaseUSerManager to use email rather than username 
    # for unique identifier
    
    def create_user(self, email, password=None, **remaining_fields):
       
        # create user now with email and password
        
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email) # cleans up text field so data is consistent
        user = self.model(email=email, **remaining_fields) # **reamaning passes the remaing field if their are any
        user.set_password(password) # hashes password django uses PBKDF2 with a SHA-256 hash
        user.save()
        return user

    def create_superuser(self, email, password, **remaining_fields):
        # create superuser with email and password 
        
        remaining_fields.setdefault("is_staff", True)
        remaining_fields.setdefault("is_superuser", True)
        remaining_fields.setdefault("is_active", True)

        if remaining_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if remaining_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **remaining_fields)
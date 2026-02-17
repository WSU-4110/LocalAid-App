
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import CustomUser
from rest_framework import status
from rest_framework.authtoken.models import Token


from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# I wanna handle sign up, login, creation, deletion, and logout here
class SignupView(APIView):
    # allows unauthorized users to run this call
    permission_classes = [AllowAny]
    def post(self, request):

        
        print("calling signup")
        # our json body from react post request
        data = request.data
        print(data)
        # now we check to see if email has been taken already

        if CustomUser.objects.filter(email=data['email']).exists():
            return Response({"ok" : False, "error": "Email taken already"}, status=status.HTTP_400_BAD_REQUEST)
        # create user object
        user = CustomUser.objects.create_user(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        

        return Response({"ok":True}, status=status.HTTP_201_CREATED)
     
    
class LoginView(APIView):
    def post(self,request):
        print("trying to get user")
        try:
            user = CustomUser.objects.get(email = request.data["email"])
        except CustomUser.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
 
        if not user.check_password(request.data["password"]):
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND) # keep error messages the same for secruity

        
        token_obj = Token.objects.get_or_create(user=user) # create/get authorization token 
        # returns obj of token key and boolean operator telling if it was created
        token_instance = token_obj[0] # not string
        token_value = token_instance.key # converts to string so it can be sent thru json
        return Response({"ok":True, "token": token_value, "user": {"email": user.email, "name": user.name}},
         status=status.HTTP_200_OK) 
     
         

class TokenCheckView(APIView): # WIP
    authentication_classes = [TokenAuthentication] # logs in user with token, will search request for "Authorization: Token fjsdklfjsdklfjsd" in the header. 
    # if found it will set request.user = current_user
    permission_classes = [IsAuthenticated] # only allow logged in users
    def get(self,request):
        return Response({"ok":True, "email" : request.user.email, "name" : request.user.name}, status=status.HTTP_200_OK)      
    
    
    

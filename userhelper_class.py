# user_helper.py

class UserHelper:
    def __init__(self, username):
        self.username = username

    def is_valid_username(self):
        return len(self.username) >= 5

    def greet_user(self):
        return f"Welcome, {self.username}!"

    def get_username_uppercase(self):
        return self.username.upper()

    def has_numbers(self):
        return any(char.isdigit() for char in self.username)

    def reverse_username(self):
        return self.username[::-1]

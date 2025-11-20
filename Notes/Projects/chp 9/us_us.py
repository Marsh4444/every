class User:
    """ creating a class user"""


    def __init__(self, first_name, last_name, profile_picture, user_age, login_attempts):
        """Initialing  user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
        self.user_age = user_age
        self.login_attempts = login_attempts


    def describe_user(self):
        """prints a summary of the user's information"""
        print(f"\nThis is the summary of your profile: full name is a {self.first_name} {self.last_name}, age is {self.user_age} and profile picture is {self.profile_picture}")


    def greet_user(self):
        """prints a message that greet the user"""
        print(f"\nGood day {self.first_name}, welcome on board!")


    def increment_login_attempts(self):
        """Increments the value of loin attempts by 1"""
        self.login_attempts += 1
        #print(f"You have increased your login by {self.login_attempts}")
        return self.login_attempts


    def reset_login_attempts(self):
        """That reset the value of login attempts"""
        self.login_attempts = 0
        return self.login_attempts
        

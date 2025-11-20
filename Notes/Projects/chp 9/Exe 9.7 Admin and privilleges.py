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

class Privileges:
    """A simple attempt to model the privilege an Admin as"""

    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        """initialing attributes of an Admin"""
        self.privileges = privileges

    def show_privileges(self):
        """Print stament discribing the privileges An Admin as"""
        for self.privilege in self.privileges:
            print(f"\nThis is the set of privilege an admin as: {self.privilege}")

    def upgrade_privileges(self):
        """updates privileges"""
        self.privileges = 'your privilege as been updated'
        print(f"\n{self.privileges}: check the portal")

class Admin(User):
    """Represent special kind of user"""

    def __init__(self, first_name, last_name, profile_picture, user_age, login_attempts):
        """Initializes attributes of the parentclass
            THe initialize attributes specific function to Users
        """
        super().__init__(first_name, last_name, profile_picture, user_age, login_attempts)
        self.privileges = Privileges()

#    def describe_privileges(self):
#        """lists the administrators set of privileges"""
#        for self.privilege in self.privileges:
#            print(f"\nThis is the set of privilege an admin as: {self.privilege}")





            
first_user = Admin('James','Allen','smiley face',23,3)
first_user.privileges.show_privileges()
first_user.privileges.upgrade_privileges()

#first_user.describe_user()
#first_user.greet_user()
#l_a = first_user.increment_login_attempts()
#print(f"\nThis is your number of attempts: {l_a}")
#print(f"\nYour number of attempts have been rested to: {first_user.reset_login_attempts()}")

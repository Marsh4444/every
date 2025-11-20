from us_us import User



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





            
#first_user.describe_user()
#first_user.greet_user()
#l_a = first_user.increment_login_attempts()
#print(f"\nThis is your number of attempts: {l_a}")
#print(f"\nYour number of attempts have been rested to: {first_user.reset_login_attempts()}")

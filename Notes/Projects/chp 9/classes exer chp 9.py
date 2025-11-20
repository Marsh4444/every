class Resturant:
    """a simple atempt to model a resturant."""


    def __init__(self, resturant_name, cuisine_type):
        """gives us info about the resturant and the cuisine type."""
        self.name = resturant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        self.number_served = 23

    
    def describe_resturant(self):
        """prints info about the name and the cuisine type """
        print(f"\nThis is the name of the resturant: {self.name}")
        print(f"\n\nThis is the type of the cuisine: {self.cuisine}")


    def open_resturant(self):
        """prints a message that indicates the resturant is open"""
        print(f"\n\n{self.name} is now open 'place your order now'")


    def read_number_served(self):
        """ Prints number of served customers"""
        print(f"\n{self.number_served} number of customers have been served")


    def set_number_served(self, serve):
        """Lets me see the number of customers that have been served."""
        self.number_served = serve


    def increment_number_served(self, customers_served):
        """Lets us increment the number of customers who have been served"""
        self.number_served += customers_served
        
resturant = Resturant('Tastyquest', 'Melon')
#print(resturant.read_number_served())
resturant.set_number_served(500)
resturant.read_number_served()
resturant.increment_number_served(57)
resturant.read_number_served()




#my_resturant = Resturant('tastyquest', 'beef')
#my_resturant.describe_resturant()
#my_resturant.open_resturant()

#my_resturant = Resturant('abj', 'milk')
#my_resturant.describe_resturant()
#my_resturant.open_resturant()

#my_resturant = Resturant('lagfood', 'goat')
#my_resturant.describe_resturant()
#my_resturant.open_resturant()



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
        

    
first_user = User('James','Allen','smiley face',23, 3)
first_user.describe_user()
first_user.greet_user()
l_a = first_user.increment_login_attempts()
print(f"\nThis is your number of attempts: {l_a}")
print(f"\nYour number of attempts have been rested to: {first_user.reset_login_attempts()}")















        















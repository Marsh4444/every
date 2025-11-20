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

#made a child class that takes all methods and attribute from the parent class Resturant.
class IceCreamStand(Resturant):
    """REspresent aspect of the resturant specific to resturant"""

    def __init__(self, resturant_name, cuisine_type):
        """initializing attributes of the parent class."""
#this function allows us to call a method from the parent class
        super().__init__(resturant_name, cuisine_type)
        self.flavours = ['vanilla','chocolate','strawberry']

    def describe_flavour(self):
        """Prints the flavours"""
        print(f"\nThis is all the flavour thats available: {self.flavours}")

my_ice_cream_stand = IceCreamStand('Tasty','Melon')
my_ice_cream_stand.describe_flavour()



























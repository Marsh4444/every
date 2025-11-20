class Dog:
    """A simple attempt to model a dog."""  


    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
 

    def sit(self): 
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")


    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()


class Car:
    """A simple attempt to represent a car."""


    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Prints a statement showing cars milleage"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
    #    """Set the odometer reading to the given value."""
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

        
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
    

    
#my_new_car = Car('audi', 'a4', 2019)
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()


#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#INHERITANCE

class Car:
    
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

#takes info required to make a car instance.
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

#a special function that allows us to call a method from the parent class    super().__init__(make, model, year)

#made an instance of the electric car and assign it to the variable my_tesla
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


#ADDING ATTRIBUTE TO SPECIFY THE ELECTRIC CAR


class Car:
    
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

#takes info required to make a car instance.
    def __init__(self, make, model, year):
        """Initialize attributes of the parentclass
            Then initialize attributes specufuc to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

#a special function that allows us to call a method from the parent class    super().__init__(make, model, year)


    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"\nThis car has a {self.battery_size}-kWh battery.")

#made an instance of the electric car and assign it to the variable my_tesla
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Instances as Attributes


class Car:
    
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
            print(f"This car can now go about {range} miles on {self.battery_size}% charge.")

        elif self.battery_size == 100:
            range = 315
            print(f"This car can now go about {range} miles on {self.battery_size}% charge.")


    def battery_upgrade(self):
        """Checks the battery size and the capacity"""
        self.battery_size = 100
        print(f"\nThe battery size as now been upgraded to: {self.battery_size}")
        
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

#takes info required to make a car instance.
    def __init__(self, make, model, year):
        """Initialize attributes of the parentclass
            Then initialize attributes specufuc to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

#a special function that allows us to call a method from the parent class    super().__init__(make, model, year)


#    def describe_battery(self):
#        """Print a statement describing the battery size"""
#        print(f"\nThis car has a {self.battery_size}-kWh battery.")

#made an instance of the electric car and assign it to the variable my_tesla
my_tesla = ElectricCar('tesla', 'model s', 2019)
#print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.battery_upgrade()
my_tesla.battery.get_range()





































































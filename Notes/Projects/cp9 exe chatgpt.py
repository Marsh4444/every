class Car:
    """COntains the atributes of cars"""

    def __init__(self, brand, year, mileage):
        """Initializes the properties of a car"""
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def car_distance(self, miles):
        """increase the milleage of a car"""
        self.mileage += miles
        return self.mileage

    def car_details(self):
        """Prints the cars info"""
        return f"{self.year} {self.brand} {self.mileage}"


my_auto = Car('Toyota', 2021, 10)
print(my_auto.car_distance(20))
print(my_auto.car_details())

    

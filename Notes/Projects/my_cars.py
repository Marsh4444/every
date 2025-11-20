#from Char import Car, ElectricCar

#my_beetle = Car('volkswagen', 'beetle', 2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = ElectricCar('tesla','roadster',2019)
#print(my_tesla.get_descriptive_name())



import Char

my_beetle = Char.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = Char.ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.year)
print(my_tesla.model)


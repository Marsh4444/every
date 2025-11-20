from Char import Car
#the stament above tells python to open car module and import the class Car

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 26
my_new_car.read_odometer()


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

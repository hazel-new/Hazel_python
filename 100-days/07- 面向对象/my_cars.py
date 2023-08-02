# from car import Car, ElectricCar
#
# my_beetle = Car('volkswagen', 'battle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())
#
# from car import Car, ElectricCar


import car

my_beetle = car.Car('volkswagen', 'battle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
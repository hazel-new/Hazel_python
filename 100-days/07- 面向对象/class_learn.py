# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# # my_dog.roll_over()
#
# print("Your dog's name is " + your_dog.name.title() + ".")
# print("Your dog is " + str(your_dog.age) + " years old.")
# your_dog.sit()


# practice 9-1
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print("The info:" + self.restaurant_name + " & " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print("The restaurant is working!")
#
#
# restaurant = Restaurant('KFC', "cook")
# restaurant2 = Restaurant('KFC2', "cook2")
# restaurant3 = Restaurant('KFC3', "cook3")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
# restaurant.open_restaurant()


# practice 9-3
# class User():
#     def __init__(self, first_name, last_name, *user_info):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_info = user_info
#
#     def describe_user(self):
#         print("The user info is: " + self.first_name + " " + self.last_name)
#
#     def greet_user(self):
#         print("Hello, " + self.first_name + " " + self.last_name + ", welcome!")
#
#
# user1 = User("alice", "wang")
# user1.describe_user()
# user1.greet_user()
#
# user2 = User("martin", "li")
# user2.describe_user()
# user2.greet_user()


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#
# # my_new_car = Car('audi', 'a4', 2016)
# # print(my_new_car.get_descriptive_name())
# # # my_new_car.read_odometer()
# # # my_new_car.odometer_reading = 23
# # my_new_car.update_odometer(23)
# # my_new_car.read_odometer()
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# practice 9-4
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print("The info:" + self.restaurant_name + " & " + self.cuisine_type)
#
#     def open_restaurant(self):
#         print("The restaurant is working!")
#
#     def set_number_served(self, numbers):
#         self.number_served = numbers
#
#     def increment_number_served(self, add_number):
#         self.number_served += add_number
#
#     def read_number(self):
#         print("There are " + str(self.number_served))
#
#
# restaurant = Restaurant('KFC', "cook")
# restaurant.describe_restaurant()
# restaurant.set_number_served(34)
# restaurant.increment_number_served(20)
# restaurant.read_number()

# # practice 9-5
# class User():
#     def __init__(self, first_name, last_name, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = login_attempts
#
#     def describe_user(self):
#         print("The user info is: " + self.first_name + " " + self.last_name)
#
#     def greet_user(self):
#         print("Hello, " + self.first_name + " " + self.last_name + ", welcome!")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_loging_attempts(self):
#         self.login_attempts = 0
#
#
# user = User('alice', 'wang', 5)
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)
# user.reset_loging_attempts()
# print(user.login_attempts)


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def fill_gas_tank(self):
#         print("This car should has a gas tank!")
#
#
# class Battery():
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kwh battery.")
#
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         # self.battery_size = 70
#         self.battery = Battery()
#
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + '-kwh battery.')
#
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank.")
#
#
# # my_audi = Car('audi', 'a4', 2016)
# # print(my_audi.get_descriptive_name())
# # my_audi.fill_gas_tank()
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# # my_tesla.describe_battery()
# # my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()


# practice 9-6
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.favors = ['sweet', 'color', 'fruit']
#
#     def show_favors(self):
#         for favor in self.favors:
#             print(favor)
#         # print(self.favors)
#
#
# icecreamstand = IceCreamStand('KFC', 'cook')
# icecreamstand.describe_restaurant()
# icecreamstand.show_favors()

# # practice 9-7
# class User():
#     def __init__(self, first_name, last_name, login_attempts):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = login_attempts
#
#     def describe_user(self):
#         print("The user info is: " + self.first_name + " " + self.last_name)
#
#     def greet_user(self):
#         print("Hello, " + self.first_name + " " + self.last_name + ", welcome!")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_loging_attempts(self):
#         self.login_attempts = 0
#
#
# class Privileges():
#     def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print("The Admin's privileges are: ")
#         for privilege in self.privileges:
#             print(privilege)
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, login_attempts):
#         super().__init__(first_name, last_name, login_attempts)
#         self.privileges = Privileges()
#
#
# admin = Admin('Alice', 'Wang', 5)
# admin.privileges.show_privileges()


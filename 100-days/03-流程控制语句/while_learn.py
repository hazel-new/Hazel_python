# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# prompt = "\nTell me something, and I will report it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will report it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\nEnter 'quit' when you are finished."
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# 练习
# prompt = "Please input the toppings: "
# prompt += "\nEnter 'quit' to end the program."
#
# while True:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         break
#     else:
#         print("We will add " + toppings + " in the pizza.py!")

# 三种方式实现while循环跳出
# prompt = "How old are you? "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("You're free!")
#     elif (age >= 3) and (age <= 12):
#         print("You need to pay $10.")
#     else:
#         print("You need to pay $15.")

# active = True
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#     else:
#         age_number = int(age)
#         if age_number < 3:
#             print("You're free!")
#         elif (age_number >= 3) and (age_number <= 12):
#             print("You need to pay $10.")
#         else:
#             print("You need to pay $15.")

# age = ""
# while age != 'quit':
#     age = input(prompt)
#     if age != 'quit':
#         age_number = int(age)
#         if age_number < 3:
#             print("You're free!")
#         elif (age_number >= 3) and (age_number <= 12):
#             print("You need to pay $10.")
#         else:
#             print("You need to pay $15.")

# 将用户从一个列表放到另一个列表
# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# 删除列表元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# 用户输入填充字典
# responses = {}
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
#
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name.title() + " would like to climb " + response.title() + ".")

# # 练习7-8
# sandwich_orders = ['tuna', 'pastrami', '3sand']
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I made your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)
#
# print("\nThe finished sandwiches are: ")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# # 练习7-9
# sandwich_orders = ['tuna', 'pastrami', '3sand', 'pastrami', '4sand', 'pastrami', '2sand','pastrami']
# print("Sorry, the pastrami has sold out! \n")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# finished_sandwiches = []
# while sandwich_orders:
#     sandwich_making = sandwich_orders.pop()
#     print("I made your " + sandwich_making + " sandwich.")
#     finished_sandwiches.append(sandwich_making)
#
# print("\nFinished sandwiches are: ")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# 练习7-10
places = {}
active = True

while active:
    name = input("\nWhat's your name? ")
    place = input("Which place you want to visit? ")
    places[name] = place

    new_person = input("Any new person to ask? (yes/no) ")
    if new_person == 'no':
        active = False

print("\n--- Results ---")
for name, place in places.items():
    print(name.title() + " wants to visit " + place.title() + ".")

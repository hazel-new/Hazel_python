# print(input("input here: \n"))

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print(name)

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# 练习
# car_type = input("Which car you want to lend? ")
# if car_type == 'subaru':
#     print("Let me see if I can find you a Subaru.")
# else:
#     print("You can check in another line.")

# user_num = input("Please tell me how many people will have lunch here? ")
# user_num = int(user_num)
# if user_num >= 8:
#     print("Sorry, we have no table now.")
# else:
#     print("Yes, we have a table for you.")

number = input("Please input a number: ")
number = int(number)
if number % 10 == 0:
    print("This number is an integer multiple of 10.")
else:
    print("This number is not an integer multiple of 10.")
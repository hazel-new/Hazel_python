# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
#
# print("\nFinished making your pizza.py!")

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("\nFinished making your pizza.py!")
# else:
#     print("Are you sure you want a plain pizza.py?")

# available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushroom', 'frech fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry,we don't have" + requested_topping + ".")
#
# print("\nFinish making your pizza.py!")


# 练习5-8
# user_lists = ['admin', 'jack', 'tom', 'jerry', 'alice']
#
# for user_list in user_lists:
#     if user_list == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print("Hello " + user_list.title() + "," + " thank you for logging in again.")

# 练习5-9
# current_users = ['admin', 'jack', 'tom', 'jerry', 'alice']
# new_users = ['eric', 'JACK', 'Tom', 'jason', 'leo']
#
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print("Sorry, " + new_user + " has exist, please try a new one!")
#     else:
#         print(new_user.title() + " is OK. You can use this name.")

# 练习5-11
nums = list(range(1, 10))
# print(nums)
for num in nums:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print("%s" % num + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")

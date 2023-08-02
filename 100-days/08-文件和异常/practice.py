# # 10-1
# filename = 'learning_python.txt'
#
# with open(filename) as file_object:
#     '''
#     1.打印读取的整个文件
#     '''
#     # contents = file_object.read()
#     # print(contents.rstrip())
#
#     '''
#     2.遍历文件对象
#     '''
#     # for line in file_object:
#     #     print(line.rstrip())
#
#     '''
#     3.各行存储在一个列表中，with外打印
#     '''
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())
#

# # 10-2
# filename = 'learning_python.txt'
#
# with open(filename) as file_object:
#     # contents = file_object.read()
#     # c_type = contents.replace('Python', 'C')
#     # print(c_type)
#
#     lines = file_object.readlines()
#
# for line in lines:
#     c_type = line.replace('Python' , 'C')
#     print(c_type.rstrip())

# # 10-3
# user_info = input("Please input your name: ")
# filename = 'guest.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write(user_info)

# # 10-4
# filename = 'guest.txt'
#
# while True:
#     user_info = input("Please input your name, and quit by enter 'q': ")
#     if user_info == 'q':
#         break
#     else:
#         print("Welcome, " + user_info.title())
#         with open(filename, 'a') as file_object:
#             file_object.write(user_info.title() + "\n")


# # 10-5
# filename = 'reason.txt'
#
# while True:
#     user_info = input("Why do you love program? You can enter 'q' for quit. \n")
#     if user_info == 'q':
#         break
#     else:
#         with open(filename, 'a') as file_object:
#             file_object.write(user_info + "\n")

# # 10-6/10-7
# print("Tell me 2 numbers, and I'll add them.\n Put 'q' to quit.")
#
# while True:
#     first_num = input("First number: ")
#     if first_num == 'q':
#         break
#     second_num = input("Second number: ")
#     if second_num == 'q':
#         break
#     try:
#         added = int(first_num) + int(second_num)
#     except ValueError:
#         print("Please put a number.")
#     else:
#         print(added)

# # 10-8/10-9
# filename = 'cat.txt'
#
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
#         print(contents)
# except FileNotFoundError:
#     # print("Can't find the file.")
#     pass


# # 10-10
# def word_count(fielname):
#     try:
#         with open(fielname) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         print("Sorry, can't find this book.")
#     else:
#         # words = contents.split()
#         # words_num = len(words)
#         # print("The " + fielname + " has " + str(words_num) + " words.")
#         words = contents.lower().count('the')
#         print("The " + fielname + " has " + str(words) + " 'the'. ")
#
#
# file_names = ['alice.txt', 'siddhartha2.txt', 'moby_dict.txt', 'little_women.txt']
# for file_name in file_names:
#     word_count(file_name)


# 10-11
import json


def get_stored_number():
    filename = 'favorite_num.json'
    try:
        with open(filename) as f_obj:
            favorite_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_num


def get_new_number():
    favorite_num = input("Please put your favorite number: ")
    filename = 'favorite_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num, f_obj)
    return favorite_num


def read_num():
    favorite_num = get_stored_number()
    if favorite_num:
        print("I know your favorite number! It's " + favorite_num)
    else:
        favorite_num = get_new_number()
        print("I know your favorite number again! It's " + favorite_num)


read_num()



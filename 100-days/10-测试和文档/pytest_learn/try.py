import os
import sys
from pprint import pprint
import configparser

# os标准库
# mo_path = os.path.dirname(__file__)
# print(mo_path)
# ro_path = os.path.dirname(mo_path)
# print(ro_path)
# co_path = os.path.join(ro_path, 'config')
# print(co_path)

# # 转义字符
# print('what\'s your name?')
#
# # format方法
# age = 25
# name = 'lisa'
# print("My name is {} and age is {}.".format(name,age))

# # sys标准库
# # pprint(sys.version_info[0])
# print("this command:\n", sys.argv)

# # configparser 标准库
# config = configparser.ConfigParser()
# # configfile = config.read(r'C:\Users\elihair\OneDrive - Ericsson AB\0_My Work\7-DSI\NW Automation\elihair_study\networkAuto_elihair\config\config.ini')
# config.read(r'C:\Users\elihair\OneDrive - Ericsson AB\0_My Work\7-DSI\NW Automation\elihair_study\networkAuto_elihair\config\config.ini')
# # pprint(configfile)
# s = config.sections()
# print(s)
# v = config.items('hydra')
# print(v)
# ssh_username = config.get(section='Netmiko', option='device_username')
# ssh_password = config.get(section='Netmiko', option='device_passwd')
# print(ssh_username)
# print(ssh_password)

# 字典/列表
# dict_name = {'name':'wang',
#              'age': 18,
#              'color': 'green'
#              }
# dict_name = {'alice':18,
#              'mark':20,
#              'linda':16,
#              'bean':22
#
# }
# list_name = [1,2,3,4,5,6]

# print(len(dict_name))
# print(dict_name['alice'])
# print(dict_name.get('linda'))
# del dict_name['bean']
# print(dict_name.items())
# print(dict(dict_name))
# print(list(dict_name))
# dict_name['a'] = 45
# dict_name['b'] = 23
#
# for name, age in dict_name.items():
#     print('name is {}, age is {}'.format(name,age))

# print(len(list_name))
# print(list_name[2])
# print(list_name)
# print(list(list_name))


# list2 = [
#     {
#         'a':1,
#         'b':2
#     },
#     {
#        'c':3,
#        'd':4
#     }
# ]
#
# print(list2)




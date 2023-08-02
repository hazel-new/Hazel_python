# re.sub 这个函数的作用是字符串的替换，之前的findall都是查找

import re

language = 'PythonC#JavaC#PHPC#'


# r = re.sub('C#', 'GO', language, 1)  # 根据函数参数意义定义替换
# print(r)
# language = language.replace('C#', 'GO') # 和sub类似功能
# print(language)


def convert(value):  # convert和value都是随便命名的
    matched = value.group()  # .group是个什么节奏？
    # print(value)  # value 是一个对象
    return '!!' + matched + '!!'


r = re.sub('C#', convert, language)
print(r)

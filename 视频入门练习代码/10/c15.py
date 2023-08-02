# 把函数作为参数传递

import re
s = 'A83C72D1D8E67'


def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'  # return 只能操作字符串
    else:
        return '0'


r = re.sub('\d', convert, s)  # 每找到一个数字，调用convert一次
print(r)

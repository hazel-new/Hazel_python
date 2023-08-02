# 概括字符集
# \d \D  数字，非数字字符
# \w \W 单词, 非单词字符
# \s \S 空白，非空白字符
# . 匹配除换行符\n之外其他所有字符


import re

a = 'python 11\t11java&___6789\np\rhp'

r = re.findall('\s', a)
p = re.findall('\w', a)
print(r)
print(p)


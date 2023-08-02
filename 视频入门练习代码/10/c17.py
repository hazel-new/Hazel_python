# group

import re

s = 'life is short, i use python, i love python'
# r = re.search('life(.*)python', s)  # 从字符串首字母开始搜索，找到符合的就返回这个字符
# print(r.group(1))  # 0 记录的是正则表达式完整匹配结果，想指定要改成1；用findall没这个问题

# r = re.findall('life(.*)python', s)
# print(r)

r = re.search('life(.*)python(.*)python', s)
# print(r.group(0))
# print(r.group(1))
# print(r.group(2))
print(r.group(0, 1, 2))
print(r.groups())  # 跟上一行相比，只返回括号里的内容

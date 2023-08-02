# re.match
# re.search
# 这两个函数没有findall好用

import re
s = '83C72D1D8E67'

r = re.match('\d', s)  # 从字符串首字母开始匹配，不match就返回空
print(r.span())
r1 = re.search('\d', s)  # 从字符串首字母开始搜索，找到符合的就返回这个字符
print(r1.group())
r2 = re.findall('\d', s)  # 返回所有值，推荐使用
print(r2)

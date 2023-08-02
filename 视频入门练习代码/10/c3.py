import re

# 正则表达式主要由普通字符和元字符组成的，主要学习元字符
# 'Python' 是普通字符，'\d' 是元字符
a = 'C0C++7Java8C#9Python|6Javascript'

# r = re.findall('\d', a)  # \d表示数字0-9
r = re.findall('\D', a)  # \D表示非数字字符
print(r)

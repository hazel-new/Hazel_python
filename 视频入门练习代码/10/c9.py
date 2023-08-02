# 边界匹配
# ^，表示从字符串的开头开始匹配
# $，表示从字符串的末尾开始匹配
import re

qq = '100000001 '
# 4~8位之间的QQ号

# r = re.findall('^000', qq)
# r = re.findall('000$', qq)
r = re.findall('000$', qq)

print(r)

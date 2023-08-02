import re  # 模块re里有很多方法来操作正则表达式

a = 'C0C++7Java8C#9Python|6Javascript'

r = re.findall('Python', a)
# 规则
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')

# print(r)

# print(a.index('Python') > -1)
# print('Python' in a)

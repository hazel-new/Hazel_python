# import c9
#
# print(c9.a)

# import t.c11
#
# print(t.c11.b)

# from t.c11 import *
#
# print(b)
# print(c)
# print(d)


# 代码太长，可以在末尾加反斜杠\实现换行
# 推荐用括号实现换行

# from c9 import a,b, \
#     c

from c9 import  (a,b,
                 c)
print(a)
print(b)
print(c)
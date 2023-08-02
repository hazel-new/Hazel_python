#  参数
#  1. 必须参数
#  2. 关键字参数
#  3. 默认参数


def add(x, y):
    result = x + y
    return result


# 关键字参数，明确指定给的参数值时给哪个形参的
# 增加代码可读性
c = add(y=3, x=2)

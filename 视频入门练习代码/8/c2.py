# 函数定义
# def funcname(parameter_list):
#     pass

# 设置递归最大次数，超过默认的995次
# import sys
# sys.setrecursionlimit(1000000)

# 1.实现两个数字的相加
# 2.打印输入的参数


def add(x, y):  # 形式参数，形参
    result = x + y
    return result


def print_code(code):
    print(code)
    return  # 遇到return，函数就终止了，后面的不会运行了
    print(code)


# a = add(1, 2)  # 执行后没有print，3暂时不会出现在屏幕上
# b = print_code('python')  # 先出现print出来的‘python’，没有return将会print出None
#
# print(a, b)  # 打印出3和None

a = add(1, 2)  # 实际参数，实参
b = print_code('python')

print(a, b)
# 函数式编程
# 闭包： 概念跟变量的作用域有关
# 定义：闭包 = 函数（curve(x)） + 环境变量 a (函数定义时候外部变量但不是全局变量，curve_pre()里，curve（）外）
# 闭包的作用： 把函数相关现场保存起来了
#


# a = 25  # 全局变量

def curve_pre():
    a = 25  # 环境变量

    def curve(x):
        return a*x*x
    return curve  # 1. 函数可以作为一个返回结果


# curve()  # 作用域只在curve_pre里面
a = 10
f = curve_pre()  # 2.函数可以赋值给另一个变量f, f变成函数
print(f.__closure__)  # 内置变量
print(f.__closure__[0].cell_contents)  # 内置变量的值 a = 25
print(f(2))










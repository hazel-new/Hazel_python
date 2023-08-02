def f1():
    a = 10

#     def f2():
#         a = 20  # a此时会被python认为是一个局部变量，不会影响外部变量
#         print(a)
#
#     print(a)  # 2. 第一句，打印全局变量10
#     f2()  # 3. 运行f2, 打印内部局部变量20
#     print(a) # 4. 打印全局变量10
#
#
# f1()  # 1. 从外向内运行

    def f2():
        # a = 20
        c = 20 * a  # 要用到外面的a，否则会认为是局部变量，也不是闭包
        # return  a
    return f2


f = f1()
print(f)
print(f.__closure__)
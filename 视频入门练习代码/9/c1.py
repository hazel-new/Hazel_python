# 面向对象
# 有意义的面向对象的代码
# 类、对象
# 类的实例化
# 类最基本的作用：封装（代码）
# 类和对象：类就像一个模板，可以通过这个模板产生很多个对
# 不同的对象：类里变量值不一样，比如name和age不一样的student


class Student():  # 类定义
    # 类体
    # 定义变量(数据成员)
    # name = 'le'  # 全局变量
    # age = 0
    # 一个班级里所有学生的总数
    sum = 0

    # ‘类变量’跟 ‘实例变量’的区别：
    # 类变量是跟类相关的变量，上面的两个变量name和age是类变量
    # 实例变量是跟对象相关的变量，实例变量是用self.关键字（也可以用其他的，但是python推荐self）来定义的，比如下面__init__里面的变量

    def __init__(self, name, age):
        # 构造函数
        # 特点：自动调用，只能返回None（一般不会定义return）
        # 作用：让模板生成不同的对象
        # 一般用来放类的初始化对象的属性
        # 下面的才是实例变量, 并给实例变量赋值
        self.name = name  # 等号后面的name跟括号里的是一样
        self.age = age
        # print('student')
        # return None

    # 设计类：刻画学生行为与特征；类设计好不好主要看能否抓住行为和特征
    def do_homework(self):
        print('homework')

    # # 定义函数（方法）,类里的函数跟在模块里的函数有区别,必须加上self
    # def print_file(self):
    #     print('name:' + self.name)  # 变量必须由self.来调用
    #     print('age:' + str(self.age))
    # # 类只负责定义，不负责执行，执行需要放在类的外部，类跟模块的区别
    # # print_file()  # TypeError: print_file() missing 1 required positional argument: 'self'


# 打印行为放到这个类更合适。
# class Printer():
#     def print_file(self):
#         print('name:' + self.name)  # 变量必须由self.来调用
#         print('age:' + str(self.age))


# 另一个类定义
# class StudentHomework():
#     homework_name = ''

#
# # 实际项目中不建议把类和执行类的实例化放在一起，一个模块放类，其他模块调用
# student = Student()  # 类的实例化，相当于其他函数的new
# student.print_file()  # 调用类下面的方法

# 方法和函数的区别
# C、C++里称为函数，JAVA、C#里称为方法
# 方法：面向对象里的一个概念，设计层面（面向对象更加关注代码的设计，比如封装概念），比如类里的叫方法
# 函数：过程，程序运行、过程式的一种称谓， 比如模块里的定义叫函数
# 变量：在模块里称为变量，在类里称为数据成员
# 面向对象：JAVA、C#，类
# 方法：def print_file():
# 数据成员: age = 0
# 过程：C、C++，模块
# 函数: def print_file():
# 变量: age = 0

# student1 = Student('石敢当', 18)  # 构造函数里有参数，这里就必须要传入参数
# a = student1.__init__()  # 会打印两次，因为构造函数的调用是自动进行的，实例化的时候python会自动调用__init函数，但是也可以显式调用。
# print(a)
# print(type(a))

# student2 = Student()
# student3 = Student()

# print(id(student1))
# print(id(student2))
# print(id(student3))

# 实例化，对象
student1 = Student('石敢当', 18)
student2 = Student('喜小乐', 19)
print(student1.name)  # 大部分语言调用都是用.，只有PHP用的是->
print(student2.name)
print(Student.sum)

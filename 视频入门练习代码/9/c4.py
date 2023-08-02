# 类变量，实例变量，实例方法的引用方法
# 类方法, 关联的是类本身
# 实例方法，关联的是对象


class Student():
    # 类变量
    name = 'le'
    age = 0
    sum1 = 0

    # 实例方法，定义的时候第一个参数一定要加self，python默认的；调用的时候不用对self传参
    # 其他语言不需要显性显示self，比如用this，python里也可以改成this
    # 显胜于隐
    # 构造函数可以看待成特殊的实例方法，其他行为基本一样
    # 构造函数跟普通实例方法的区别：
    # 1.调用方式不同：前者是调用类后面的括号的方式student1 = Student('石敢当', 18)，后者是通过对象调用student1.do_homework()
    # 2.意义不同：前者是初始化类的各种特征，后者是描述类的行为的
    # 构造函数/实例方法：
    # 通常用来操作实例变量
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        # print(sum1)  # 实例方法如何正确访问类变量
        # print(Student.sum1)
        print(self.__class__.sum1)
        # print(age)
        # print(self.name)  # 访问实例变量最好加上self.
        # print(self.__dict__)
        # print(name)  # 访问实例变量最好加上self.

    def do_homework(self):
        print('homework')


# 实例化，对象
student1 = Student('石敢当', 18)
# student1.do_homework()
# print(student1.__dict__)  # __dict__是用来存储对象属性的一个字典，其键为属性名，值为属性的值。
# print(Student.__dict__)
print(student1.name)
# print(Student.name)
print(Student.sum1)

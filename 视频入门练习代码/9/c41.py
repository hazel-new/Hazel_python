# 类变量，实例变量，实例方法的引用方法
# 类方法, 关联的是类本身
# 实例方法，关联的是对象


class Student():
    # 类变量
    # name = 'le'
    # age = 0
    sum = 0

    # 构造函数/实例方法：
    # 通常用来操作实例变量
    # 实例方法，定义的时候第一个参数一定要加self，python默认的；调用的时候不用对self传参
    # 其他语言不需要显性显示self，比如用this，python里也可以改成this
    # 显胜于隐
    # 构造函数可以看待成特殊的实例方法，其他行为基本一样
    # 构造函数跟普通实例方法的区别：
    # 1.调用方式不同：前者是调用类后面的括号的方式student1 = Student('石敢当', 18)，后者是通过对象调用student1.do_homework()
    # 2.意义不同：前者是初始化类的各种特征，后者是描述类的行为的
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        self.score = 0
        # self.__class__.sum += 1
        # print('当前班级学生总数为：' + str(self.__class__.sum))  # 数字转变成字符串，然后做字符串连接+操作

        # print(sum1)  # 实例方法如何正确访问类变量
        # print(Student.sum1)
        # print(self.__class__.sum1)
        # print(age)
        # print(self.name)  # 访问实例变量最好加上self.
        # print(self.__dict__)
        # print(name)  # 访问实例变量最好加上self.

    # 私有和公有
    # 变量或者方法前面加上双下划线__表示这是私有的，类外面不能再调用私有方法，严格来说其实python没有私有
    # 但是前后都有__就不会认为是私有的，比如init
    # python内置变量一般会前后加__，所以最好不要再写类似命名
    # def __marking(self, score):
    def marking(self, score):
        if score < 0:
            return '不能够给别人打负分'
        self.__score = score
        print(self.name + '同学本次考试分数为：' + str(self.__score))

    # 实例方法
    def do_homework(self):
        self.__class__.sum += 1
        # print('当前班级学生总数为：' + str(self.__class__.sum))
        # print('homework')
        self.do_english_homework()  # 在类的内部调用，跟外部调用对比

    def do_english_homework(self):
        print()

    # 类方法
    # 看是否加上装饰器
    # 只跟类相关，跟对象没关系
    @classmethod  # 装饰器，前面加上这个可以让下面的成为类方法
    def plus_sum(cls):  # python建议用cls，用self也可以
        cls.sum += 1
        print(cls.sum)  # 可以访问类变量
        # print(self.name)   # 不可以访问实例变量

    # def plus_sum(self):
    #     self.sum += 1
    #     print(self.sum)

    # 静态方法
    # 一般用可以用类方法替代，不建议常用
    # 使用场景：非常纯粹的场景
    # C#里的静态方法其实类似python里的类方法
    @staticmethod
    def add(x, y):
        print(Student.sum)  # 可以访问类变量
        # print(self.name)    # 不可以访问实例变量
        print('This is a Static method')


# 实例化，对象

student1 = Student('石敢当', 18)  # 实例化了一个对象student1
student2 = Student('小诺', 18)  # 实例化了一个对象student1

result = student1.marking(59)

# student1.__score = -1  # 这里私有变量能被赋值且不报错，是因为python作为动态语言，可以通过.的方式重新添加了新的实例变量__score

# print(student1.__dict__)  # 打印结果：{'name': '石敢当', 'age': 18, 'score': 0, '_Student__score': 59, '__score': -1}
# print(student2.__dict__)  # 打印结果：{'name': '小诺', 'age': 18, 'score': 0}


# print(student1.__score)
# print(student2.__score) # 这里会报错，跟student1.__score比，就是因为没有重新添加新的实例变量
# print(student2._Student__score)  # 因为没有严格私有，全名还是能访问私有变量

# # result = student1.__marking(-1)  # 私有方法不可以调用了
# result = student1.marking(59)
# print(result)

# student1.score = -1  # 不建议这样外部赋值，score是公开的(public)，相对的是私有的(private)

# student1.do_homework()  # 调用了student1的do_homework方法， 在对象的外部调用了do_homework方法

# student1.add(1, 2)  # 对象调用静态方法
# Student.add(1, 2)  # 类调用静态方法
# student1.plus_sum()  # 对象调用类方法
# Student.plus_sum()  # 类调用类方法

# student1.do_homework() # 对象调用实例方法

# Student.plus_sum()  # 类调用类方法
# student1.plus_sum()  # 对象调用类方法，不报错但不建议

# print(student1.__dict__)  # __dict__是用来存储对象属性的一个字典，其键为属性名，值为属性的值。
# print(Student.__dict__)

# student2 = Student('喜小乐', 18)
# # student2.do_homework()
# Student.plus_sum()
# student3 = Student('小诺', 18)
# # student3.do_homework()
# Student.plus_sum()


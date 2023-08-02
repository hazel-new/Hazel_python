from c6 import Human


class Student(Human):
    # sum = 0

    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)  # 推荐使用的调用父类方法

        # Human.__init__(self, name, age)  # 在子类里调用父类的构造函数，用类来调用实例方法，记得要加上self
        # # 这里一定要加上self，而后面实例化的时候不需要加self的区别：
        # # 实例化的时候调用了构造函数，但是python机制会默认调self
        # # 这里是用类调用的构造函数，是普通方式的调用，需要把所有参数传进去

        # self.__score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        super(Student, self).do_homework()  # 调用父类里同名方法
        print('english homework')


student1 = Student('人民路小学', '石敢当', 18)
student1.do_homework()  # 这里是通过对象student1来调用的实例方法，python知道self不用加
# Student.do_homework(student1)  # 用类调用实例方法时，把对象或者任意参数传进去，这样做没意义，其他语言一般不允许。建议用对象调用实例方法
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()



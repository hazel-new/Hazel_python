# #抛出一个异常raise Exception监控。stop停止。
# for i in range(10):
#     if i>4:
#         raise Exception('抛出一个异常')
#     print(i)
# print('我很好')

# #assert 断言+条件+报错信息，不符合条件时，抛出的信息。
# t = ('hello','boy',2,2,3,1)
# print(len(t))
# assert len(t)>30,'数据少于30个' #不符合条件时，抛出的异常，中断程序

#带mesage的assert语句，断言

# #要求：验证手机号，1.11位。 2.里面都是数字，3.前三位时指定的集合['186','187','130]
# def myphone(phone):
#     if len(phone)!=11:
#         raise Exception('less than 11 numbers')
#     for i in range(len(phone)):
#         if phone[1] not in ['1','2','3','4','5','6','7','8','9','0']:
#             raise Exception('has no number string')
#     if phone[:3] not in ['186','187','130']:
#         raise Exception('not follow first 3 numbers rule')
#
# print(myphone(130888))
# print(myphone(13039820099))
# print(myphone(18598730490))
# print(myphone(18793405833))
#
#


# #类
# class Car:
#     def __init__(self,brand='',price=0,no=0):
#         self.brand=brand
#         self.price=price
#         self.__no=no
#     def openit(self):
#         print('open {} door'.format(self.brand))
#     def sellit(self):
#         self.openit()
#         print('{}sell price is {} dollar'.format(self.brand,self.price*0.8))
#     def useit(self):
#         self.__no+=1
#         self.price-=10000 if self.price>10000 else 0
#     def showno(self):
#         print(self.__no)
# mycar=Car()
# mycar.brand='广本'
# mycar.price=80000
# mycar.showno()
# print(mycar.price)


# #
# @staticmethod #声明位静态方法，不需要实例
# def getPrice():#注意
#     print(Fruit.price)
#
# def __getPrice():#私有方法，不能在类的外部调用。
#     Fruit.price=Fruit.price+5
#     print(Fruit.price)
#
# count = staticmethod(__getPrice) #静态方法
# Fruit.getPrice() #不需要实例，直接使用
# Fruit.count() #调用类的私有方法



# print('this is %s,this is %s' % ("zhang","hao")) #C %s,%d
# print('this is {}, his age is {}'.format('jerry',23)) #和上面效率差不多，没下面的高
# print("this is {0},that's {1}".format('jerry',"tom"))

# # 元组 tuple
# b=('a','b','v',1,3,5,888,9999,0000,8888)
# print(b[0:4])
# print(b[:4])
# print(b[-4:])
# print(b[:])

# tuple的解包
# a = (1,2,3,4)
# b,c,d,e =a
# print(b,c,d,e)
# z = ((1,2),(3,4))
# for x in z:
#     print(x)
# for a,b in z:
#     print(a,b)

# # 解包过程中，星号代表可变
# a = (1,2,3,4)
# print(len(a))
# b, *c =a   # b代表第一个元素，剩下其余的元素都交给c；不是特别推荐，debug会加大难度。
# print(b,c)
# # a[2]=33  #元组内元素不可改变


# #练习，如何将a和b的值互换
# a = 2
# b = 3
# a,b = b,a
# print(a,b)
#
#

##练习
# lst1 = [4,5,6,7]
# lst2 = []
# for i in range(len(lst1)): # i是索引，i=0，2，3，4
#     lst2.append(lst1[i]) #添加
#     lst1[i] = lst1[i]*2 #修改
# lst2.remove(6)  #remove具体的元素，要是已有的元素，如有重复选第一个
# a = lst2.pop(2)  #pop的是索引,可以不用变量，用变量是保存POP的内容
# print(lst1)
# print(lst2)
# print('pop的内容',a)


#不能直接复制，只是生成两个标签，指向同一个内存地址，最好用append一个一个添加


# #列表推导
# lst1=[2,3,5,7,8,99,766]
# lst2 = [x*2 for x in lst1] # 比前面练习里的append更高效
# print(lst2)
#
# lst3 = [x for x in range(10) if x%2==0]
# print(lst3)
#
# a = -4
# b = 1 if a>0 else -1
# print(b)


# #字符串创建列表的方法
# word = 'a,b,d,d,f,g,e'
# wordlst = word.split(',')
# print(wordlst)
#
# word2 = '|'.join(wordlst) #列表的字符串的拼接
# print(word2)

# #input:num='1,2,3,4,5'
# # output: lst1=[2,4,6,8,10]
#
# num = '1,2,3,4,5'
# lst = num.split(',')
# print(lst)
#
# lst1 = [int(x)*2 for x in lst]
# print(lst1)


#zip形成新的元素表
#in

# #集合 set，元素是唯一的，唯一性。无序，不支持索引
# 自然语言处理 NLP
# sen1 = '我 去 南京 参加 培训'
# sen2 = '你 也 到 南京 培训 了 吗'
# print(sen1.split())
# s1 = set(sen1.split())
# s2 = set(sen2.split())
# print(s1.intersection(s2)) #交集
#
# s3 = {'我', '北京'}
# print(s3.issubset(s1)) #判断子集

# dict1 = {'a':1,'b':2,'c':3,'d':12,'a':999}
# for k,v in dict1.items():
#     print(k,v)

# # 自然语言处理 NLP
# sen1='我 去 南京 参加 培训'
# sen2='你 也 到 南京 培训 了 吗'
# s1 = set(sen1.split())
# s2 = set(sen2.split())
# s3 = s1 | s2
# print(s3)
#
# word2id = {}
#
# for n,x in enumerate(s3):
#     word2id[x]=n
#
# print(word2id)

# #高级知识 字典的排序
# dict1 = {'a':1,'b':2,'c':3,'d':12,'a':999}
# sort_dct = sorted(dict1.items(), key=lambda e:e[1], reverse = True)
# sort_dct1 = sorted(dict1.items(), key=lambda e:e[1], reverse = False)
# sort_dct2 = sorted(dict1.items(), key=lambda e:e[0], reverse = True)
# sort_dct3 = sorted(dict1.items(), key=lambda e:e[0])
# print(sort_dct)
# print(sort_dct1)
# print(sort_dct2)
# print(sort_dct3)

# 字典的嵌套


# #生成器 yield
# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield b  #这里之后就跳出函数，暂停并返回结果。
#         a,b = b,a+b
#
#
# fib = fibonacci()
# a1 = next(fib)
# print(a1)
# print([next(fib) for i in range(10)])
#

#
# #函数里更新全局变量
# a = 999
# b = 988
# def doit(b):
#     global a  #声明使用全局变量a
#     print("外部的a：",a)
#     print("函数里的b:",b)
#     a = 3
#     return
#
# doit(2)
# print("外部变量a", a)
# print("外部变量b", b)


# #将函数作为参数传给另一个函数，面向对象的概念
# def hi():
#     return "morning!"
#
# def doit(func):
#     print("students, up")
#     print(func())  #此处要加()，否则显示运行结果地址
#     print("students,down")
#
# doit(hi) #此处不要加()


#函数的默认参数 python 3.*

# #练习题：可变参数的累加
# def mysum(*x):
#     s = 0
#     print(x)
#     for i in x:
#         s+=i #s=s+i
#     return s
# print(mysum(1,2,3))
# print(mysum(1,2,-3,-4,-5))

# 中位数，统计学使用

# #装饰器
# def a_new_decorator(a_func): #参数得是一个函数
#     def doit():
#         print("wake up")
#         a_func() #执行这个函数
#         print("have breakfast")
#     return doit #返回的是一个函数
#
# @a_new_decorator #等价于 book = a_new_decorator(book)
# def book():
#     print("read book")
#
# book()

# #装饰器的应用：日志的记录
# import functools
#
# def log()

# #带参数的装饰器
# import functools
#
# def log_with_param(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs): #**kw -> 变成字典形式 {key:value,key:value}
#             print('使用函数 %s():' % func.__name__)
#             print('函数参数 = {}'.format(*args))
#             print('自己的参数 = {}'.format(text))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @log_with_param("我是参数")
# def test(p):
#     print(p+'请起立')
#
# test('小张同学')

#装饰器的使用场景2--授权


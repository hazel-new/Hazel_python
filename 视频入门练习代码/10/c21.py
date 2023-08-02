# 序列化： 把python的数据类型向JSON字符串转化
# NOSQL数据库：MongoDB 适合存储序列化后的对象，反对把序列化后的对象以字符串的形式存到数据库里去
# JSON 对象、JSON、JSON字符串 ：第一个概念有点模糊
# JavaScript 只是实现ECMASCRIPT标准的语言之一，还有ActionScript，Typescript等这样的语言
# JSON 不是JS的附属品，某些角度看可以看成平级的语言。但是JSON大量应用在JS的交互中。
# JSON 有自己的数据类型，虽然它和JS的数据类型有些类似
# REST 服务的标准格式就是JSON

import json
# python dict向JSON str转换
# student = [
#     {'name': 'qiyue', 'age': 18, 'flag': False},
#     {'name': 'qiyue', 'age': 18}
# ]
student = {'name': 'qiyue', 'age': 18, 'flag': False}
json_str = json.dumps(student)
print(type(json_str))
print(json_str)




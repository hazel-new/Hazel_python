# JSON
# 反序列化：由字符串到语言下某种数据结构的过程， 比如JSON object -> python dict, JSON array -> python list
import json

# JSON object 对象
# json_str = '{"name":"qiyue", "age":18}'  # {}内JSON规范标准规定字符必须用双引号""，外面python就用单引号''表示字符串了

# JSON array 数组
# 把JSON的数据类型转变成Python自己的数据类型

json_str = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"qiyue", "age":18}]'

# print(type(json_str))

# # 转变成dict
# student = json.loads(json_str)  # 用load函数把json字符串转变成字典了,JS里的对象转变成了python里的字典
# print(type(student))  # 这里是字典
# print(student)  # 打印出来是字典，不是字符串
# print(student['name'])
# print(student['age'])

# 转变成列表 list []
student = json.loads(json_str)
print(type(student))
print(student)

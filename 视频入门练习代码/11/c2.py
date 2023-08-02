# 枚举: 在python里本质是一个类

# 需要导入枚举相关模块和类
from enum import Enum


# class名字可以自定义,参数是Enum
# 建议：枚举的标识名字（标签）最好全部大写，表示是常量，不能轻易更改
class VIP(Enum):
    YELLOW = 1
    # YELLOW = 2 # 报错，标签不能重复
    # GREEN = 1    # 值可以相同，只是会打印出YELLOW, 称为别名，数值相等的情况下其实是一种枚举类型，后者会成为第一个的别名，不会成为新的枚举类型
    YELLOW_ALIAS = 1  # 值相同的情况下，应该叫别名,遍历默认不打印出来
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1   # 大写了还是变量，不是常量，能更改


# # 采用枚举，调用的时候可读性强；枚举的意义在于标签而不在值
# print(VIP.GREEN)
# # VIP.YELLOW = 6  # 改值失败，保护作用

# for v in VIP:
#     print(v)

# # 遍历所有，包括别名，输出所有元素，元组格式
# for v in VIP.__members__.items():
#     print(v)


# # 遍历所有，包括别名，输出精简版
# for v in VIP.__members__:
#     print(v)


# 使用具体数值访问枚举类型的方法，可以作为类型转换使用
a = 1
print(VIP(a))

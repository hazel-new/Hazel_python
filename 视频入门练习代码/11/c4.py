# 枚举: 在python里本质是一个类
# 枚举类型，枚举的名字，枚举的值

from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 别名
class Common():
    YELLOW = 1


# print(VIP.GREEN.value)  # 枚举的值
# print(VIP.GREEN.name)   # 枚举下面标签的名字
# print(type(VIP.GREEN.name))   # 枚举的名字，是字符类型
# print(VIP.GREEN)   # 表示的枚举下面的一个类型
# print(type(VIP.GREEN))   # 枚举类型

# print(type(VIP.GREEN.name))
# print(type(VIP.GREEN))
# print(VIP['GREEN'])  # 打印出具体的枚举类型

for v in VIP:
    print(v)
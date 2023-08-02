# 枚举的比较, 不能做大小比较，能做等值比较，==， is
# 23种设计模式，单例模式，所以枚举不能实例化
# 设计模式的出现是为了解决软件工程的问题而出的方案，防止代码频繁变化，要在实际运用中
# 小公司没有用到设计模式的意义，因为经常重写或者改变，团队要统一意识和能力，否则没有必要
# 编程初期不必多关注，后期关注程序本身才有意义
# 跟环境有关，“扩展开放，修改关闭” 要权衡
# 

from enum import Enum
from enum import IntEnum, unique

# class VIP(Enum):
#     YELLOW = 1
#     GREEN = 2
#     # GREEN = 'str'  # 可以定义其他类型
#     BLACK = 3
#     RED = 4

# unique 装饰器，不允许定义重复的值
@unique
class VIP(IntEnum):  # 不允许定义Int以外的值
    YELLOW = 1
    GREEN = 2
    # GREEN = 1  #
    # GREEN = 'str'
    BLACK = 3
    RED = 4


# class VIP1(Enum):
#     YELLOW = 1
#     GREEN = 2
#     BLACK = 3
#     RED = 4


# class Common():
#     YELLOW = 1


# result = VIP.GREEN == VIP.BLACK
# result = VIP.GREEN > VIP.BLACK
# result = VIP.GREEN is VIP.GREEN

# result = VIP.GREEN == VIP1.GREEN  # 两个枚举类型比较

# print(result)


# 旅行者
# x = 0, 3步，result = 3， 再走5步，result = 8
# 关键：每次调用函数需要保持上一次函数的结果
# 非闭包方法
origin = 0


def go(step):
    global origin  # 关键，设成全局变量
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))
print(go(6))

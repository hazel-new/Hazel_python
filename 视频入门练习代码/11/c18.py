origin = 0


# 闭包的环境变量保存功能
def factory(pos):
    def go(step):
        nonlocal pos  # 强制声明不是局部变量
        new_pos = pos + step
        pos = new_pos  # pos会被认为是局部变量
        return new_pos
    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))



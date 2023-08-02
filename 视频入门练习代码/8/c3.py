# R Skill1 Skill2
#
# def damage(skill1, skill2, out/ref damage2):
#     damage1, damage2
#     return(damage1, damage2)
#     damage1
#     return damage1


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2  # 不用强制加括号，逗号隔开，自动成为元组

# 元组模式
# damages = damage(3, 6)
# print(damages[0], damages[1])
# print(type(damages))

# 序列解包
skill1_damage, skill2_damage = damage(3,6)
print(skill1_damage, skill2_damage)
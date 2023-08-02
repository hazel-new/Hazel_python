# for循环
# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")
#
# print("Thank you, everyone. That was a great magic show!")

# # practise1
# pizzas = ['ro1', 'bi2', 'hd3']
# for pizza.py in pizzas:
#     print("I like " + pizza.py.title() + " pizza.py!")
#
# print("I really love pizza.py!")

# range()
# for value in range(1,5):
#     print(value)

# list()
# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(4,11,2))
# print(even_numbers)

# # 生成乘方列表
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# # 最大值，最小值，总和
# digits = list(range(0,10))
# print(digits)
# print(max(digits))
# print(min(digits))
# print(sum(digits))

# 列表解析
# squares = [value**2 for value in range(1,11)]
# print(squares)

# 练习
# for value in range(1,21):
    # print(value)
from pprint import pprint
# nums = list(range(1, 1000001))
# # pprint(nums)
# # for num in nums:
# #     print(num)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# odd_nums = list(range(1,21,2))
# print(odd_nums)
# for odd_num in odd_nums:
#     print(odd_num)

# nums = list(range(3, 31, 3))
# print(nums)
# for num in nums:
#     print(num)

# 立方列表
# cubes = []
# for value in range(1,11):
#     cube = value**3
#     cubes.append(cube)
# print(cubes)

# 列表解析生成立方列表
# cubes = [value**3 for value in range(1,11)]
# print(cubes)

# # 切片和复制练习
# cubes = [value**3 for value in range(1,11)]
# print(cubes)
# print("The first three items in the list are:")
# print(cubes[:3])
# print("Three items form the middle of list are:")
# print(cubes[4:7])
# print("The last three items in the list are:")
# print(cubes[-3:])

pizzas = ['ro1', 'bi2', 'hd3']
friend_pizzars = pizzas[:]
pizzas.append('huf4')
friend_pizzars.append('rea5')
print("My favorite pizzas are:")
print(pizzas)
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
print(friend_pizzars)
for friend_pizzar in friend_pizzars:
    print(friend_pizzar)

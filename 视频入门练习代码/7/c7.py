# 主要是用来遍历/循环 序列或者集合、字典
# for target_list in expression_list
#   pass

# a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
# for x in a:
#     if 'banana' in x:
#         break
#     for y in x:
#         if y == 'orange':
#             break
#         print(y)
# else:
#     print('fruit is gone')

##################################################

# a = [1, 2, 3]
#
# for x in a:
#     if x == 2:
#         break
#         # continue
#     print(x)
# else:
#     print('EOF')

####################################################

# for (i=0; i<10; i++){}

#for each
# a = [1,2,3,4,5...]

for x in range(10,0,-2):
    print(x, end= ' | ' )
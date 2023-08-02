a = [1, 2, 3, 4, 5, 6, 7, 8]
# 打印出相间隔的元素

# 方法一
# for i in range(0, len(a), 2):
#     print(a[i], end=' | ')

# 方法二
b = a[0:len(a):2]
print(b)
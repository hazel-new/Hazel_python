# 大小写转换
name = " ada love"
print(name.title())
print(name.upper())
print(name.lower())

# 制表符和换行符
print("Python")
print("\tPython\tlearn")
print("\nPython")

# 字符串拼接
first_name = "tom"
last_name = "ford"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())

# 去除空白字符
language = " python "
print(language.rstrip())
print(language.lstrip())
print(language.strip())

# str()
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#test
num = 6
love = "I love " + str(num) + "" \
                              "!"
print(love)
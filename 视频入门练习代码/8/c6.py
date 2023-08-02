# def print_student_files(name, gender, age, college):
# def print_student_files(name, gender='男', age=8, college='人民路小学', teacher): 最后的teacher是非默认参数，不能放在默认参数后面，所有非默认参数都要放在前面


def print_student_files(name, gender='男', age=8, college='人民路小学'):
    print('我叫' + name)
    print('我今年' + str(age) + '岁')  # 强制把age转成str格式
    print('我是' + gender + '生')
    print('我在' + college + '上学')


print_student_files('小萌', '男', 8, '人民路小学')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files('小萌')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files('小当')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files('小乐', '女', '6')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_student_files('小果', age='7', college='光明小学', gender='女')  # 关键字参数可以不care参数顺序


# 7这个参数不能跟在关键字参数后面，SyntaxError: positional argument follows keyword argument
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print_student_files('小果', gender='女', 7, college='光明小学')

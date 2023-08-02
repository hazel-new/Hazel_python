'''
    this module is for simple program
'''

account = "que"
password = '123456'

print('Please input account')
user_account = input()

print('Please input password')
user_password = input()

if (user_account == account) and (user_password == password):
    print('success')
else:
    print('fail')



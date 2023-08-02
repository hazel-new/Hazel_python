# zip/list用法

a = ['zia','ziv','zir']
b = ['idm1','idm2','imd3']
d = zip(a,b)
# print(d)
e = list(d)
print("e is:", e)

for one_role_idm in e:
    one_role = one_role_idm[0]
    print(one_role)
    one_idm = one_role_idm[1]
    print(one_idm)
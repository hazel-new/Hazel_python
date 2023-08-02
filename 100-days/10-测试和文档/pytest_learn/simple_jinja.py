from jinja2 import Template, escape

# name = input("please input your name:")
# tm = Template("Hello {{ x }}")
# msg = tm.render(x=name)
# print(msg)

# name = 'Peter'
# age = 32
#
# tm = Template("My name is {{ x }} and I am {{ y }} years old.")
# msg = tm.render(x=name,y=age)
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getAge(self):
#         return self.age
#
#     def getName(self):
#         return self.name
#
#
# person = Person('Peter',34)
#
# tm = Template("My name is {{ x.getName() }} and I am {{ x.getAge() }} years old.")
# msg = tm.render(x=person)
# print(msg)

# person = {'name':'Person','age':34}
# # tm = Template("My name is {{ x.name }} and I am {{ x.age }} years old.")
# tm = Template("My name is {{ x['name'] }} and I am {{ x['age'] }} years old.")
# msg = tm.render(x=person)
# print(msg)

# #有问题
# data = '''
# {% raw %}
# His name is  {{ x }}
# {% endraw %}
# '''
#
# tm = Template(data)
# msg = tm.render(x='Peter')
# print(msg)

# data = '<a>Today is a sunny day.</a>'
# tm = Template("{{ x | e }}")
# msg = tm.render(x=data)
#
# print(msg)
# print(escape(data))


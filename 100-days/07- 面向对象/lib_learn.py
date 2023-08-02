# from collections import OrderedDict
#
# facorite_languages = OrderedDict()
#
# facorite_languages['jen'] = 'python'
# facorite_languages['sarah'] = 'c'
# facorite_languages['edward'] = 'ruby'
# facorite_languages['phil'] = 'python'
#
# for name, language in facorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + '.')


from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


die = Die(6)
print("one")
for i in range(1, 11):
    die.roll_die()

print("\ntwo")
die2 = Die(10)
for i in range(1, 11):
    die2.roll_die()

print("\nthree")
die3 = Die(20)
for i in range(1, 11):
    die3.roll_die()

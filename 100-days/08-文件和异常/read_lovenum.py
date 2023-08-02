import json


filename = 'favorite_num.json'
try:
    with open(filename) as f_obj:
        favorite_num = json.load(f_obj)
except FileNotFoundError:
    print("Sorry can't find the number.")
else:
    print("I know your favorite number! It's " + favorite_num)
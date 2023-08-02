# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# # 练习
# friend = {'first_name': 'leo', 'last_name': 'wang', 'age': 30, 'city': 'SH'}
# # print(friend['age'])
# for key,value in friend.items():
#     print("\nKey: " + key)
#     print("Value: " + str(value))
#
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
#     }

# for name, language in favorite_language.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# friends = ['phil', 'sarah']
# for name in favorite_language.keys():
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() + ", i see your favorite language is " +
#               favorite_language[name].title() + "!")
#
# if 'erin' not in favorite_language.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_language.keys()):
#     print(name.title() + ", thank you for taking the poll!")

# for language in favorite_language.values():
#     print(language.title())

# for langauge in set(favorite_language.values()):
#     print(langauge.title())

# 练习
# rivers = {
#     'nile': 'egypt',
#     'changjiang': 'china',
#     'yellow river': 'china'
# }
#
# for river_name, country in rivers.items():
#     print("The " + river_name.title() + " runs through " + country.title())
#
# print("\n")
#
# for river_name in sorted(rivers.keys()):
#     print(river_name.title())
#
# print("\n")
#
# for country in sorted(set(rivers.values())):
#     print(country.title())

# name_lists = ['harry', 'jen', 'leo', 'sarah', 'phil']
#
# for name_list in name_lists:
#     if name_list in favorite_language.keys():
#         print(name_list.title() + ", thanks for your joining!")
#     else:
#         print(name_list.title() + ", welcome to join the poll!")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

# aliens = []
#
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")
#
# print("Total number of aliens: " + str(len(aliens)))

# pizza.py = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra cheese'],
# }
#
# print("You ordered a " + pizza.py['crust'] + '-crust pizza.py ' +
#       "with the following toppings:")
#
# for topping in pizza.py['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }
#
# for name, languages in favorite_languages.items():
#     print("\n" + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print("\t" + language.title())

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton'
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#     }
# }
#
# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#
#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())

# # 练习6-7
# friend_0 = {'first_name': 'leo', 'last_name': 'wang', 'age': 30, 'city': 'SH'}
# friend_1 = {'first_name': 'jerry', 'last_name': 'li', 'age': 34, 'city': 'NJ'}
# friend_2 = {'first_name': 'harry', 'last_name': 'huang', 'age': 31, 'city': 'CD'}
# people = [friend_0, friend_1, friend_2]
# for friend in people:
#     print(friend)

# # 练习6-9
# favorite_places = {
#     'tom': ['jiangsu', 'anhui','shanghai'],
#     'jerry': ['yunnan', 'xian', 'sichuang', 'chongqing'],
#     'leo': ['shanxi']
# }
# for name, places in favorite_places.items():
#     print(name.title() + "'s favorite places are:")
#     for place in places:
#         print("\t" + place.title())

# 练习6-11
cities = {
    'shanghai': {
        'country': 'china',
        'population': 10000,
        'fact': 'fashion'
    },
    'nanjing': {
        'country': 'china',
        'population': 9000,
        'fact': 'history'
    },
    'chengdu': {
        'country': 'china',
        'population': 8000,
        'fact': 'life'
    }
}
for city_name, city_info in cities.items():
    print(city_name.title() + "'s information is: ")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print("\tCountry: " + country.title())
    # print("\tPopulation: %s" % population)
    print("\tPopulation: " + str(population))
    print("\tfact: " + fact.title())

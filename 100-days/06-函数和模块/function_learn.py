# def greet_user(username):
#     print("Hello, " + username.title() + "!")
# greet_user('jack')


# def display_message():
#     print("Learning function!")
#
#
# display_message()


# def favorite_book(title):
#     print("One of my favorite books is " + title.title() + ".")
#
#
# favorite_book('Alice in Wonderland')
#
#


# def describe_pet(animal_type, pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet('hamster', 'harry')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet('dog', 'willie')


# def make_shirt(size='L', logan='I Love Python'):
#     print("The shirt's size is " + size + " and the logan is " + logan.title())
#
#
# make_shirt()
# make_shirt('M')
# make_shirt(logan='Hello World!')


# def describe_city(city_name, country='china'):
#     print(city_name.title() + " is in " + country.title())
#
#
# describe_city('shanghai')
# describe_city('paris', 'french')
# describe_city('nanjing')


# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('jimi', 'hendrix', 'lee')
# print(musician)


# def build_person(first_name, last_name, age=''):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
#
#
# while True:
#     print("\nPlease tell me your name: ")
#     print("enter 'q' at any time to quit.")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")


# def city_country(city_name, country_name):
#     country = city_name.title() + ", " + country_name.title()
#     return country
#
#
# countries_1 = city_country('shanghai', 'china')
# countries_2 = city_country('stockholm', 'sweden')
# countries_3 = city_country('newYork', 'america')
# print(countries_1, "\n", countries_2, "\n", countries_3)


# def make_album(singer, album, song_num=''):
#     album_dict = {"Signer:": singer, "Album": album}
#     if song_num:
#         album_dict['Song_number'] = song_num
#     return album_dict
#
#
# while True:
#     print("\nPlease input the singer and album_name, and 'q' for quit: ")
#     s_name = input('Singer name: ')
#     if s_name == 'q':
#         break
#     a_name = input('Album name: ')
#     if a_name == 'q':
#         break
#     album_info = make_album(s_name, a_name)
#     print(album_info)

# album1 = make_album('hellen', 'world1')
# album2 = make_album('jay zhou', 'fantasy', 12)
# album3 = make_album('andy', 'beautiful')
# print(album1, "\n", album2, "\n", album3)


# def greet_users(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
#
# usernames = ['harry', 'ty', 'marfot']
# greet_users(usernames)


# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def show_magicians(name_lists):
#     print("\nOriginal list:")
#     for name_list in name_lists:
#         print(name_list.title())
#
#
# def make_great(name_lists, great_lists):
#     while name_lists:
#         current_list = name_lists.pop()
#         current_list += " the Great"
#         print(current_list)
#         great_lists.append(current_list)
#
#
# name_lists = ['jack', 'harry', 'martin']
# great_lists = []
# # make_great(name_lists, great_lists)
# make_great(name_lists[:], great_lists)
# show_magicians(name_lists)

#
# def make_pizza(size, *toppings):
#     # print("\nMaking a pizza.py with the following toppings: ")
#     print("\nMaking a " + str(size) + "-inch pizza.py with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')


# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key,value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)


# def make_sandwich(*lists):
#     print("\nMaking sandwich with: ")
#     print(lists)
#     # print("\nMaking sandwich with: " + str(lists))
#     # print("\nMaking sandwich with: %s" % lists) ## str问题？
#
#
# make_sandwich('eggs')
# make_sandwich('eggs', 'fruit')
# make_sandwich('eggs', 'fruit', 'fish')


# def build_profile(first_name, last_name, **user_info):
#     profile = {}
#     profile['First name'] = first_name
#     profile['Last name'] = last_name
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('alice', 'wang', location='shanghai', country='china')
# print(user_profile)


# def make_car(manufacturer, model, **car_info):
#     profile = {}
#     profile['Manufacturer'] = manufacturer.title()
#     profile['Model'] = model
#     for k,v in car_info.items():
#         profile[k] = v
#     return profile
#
#
# car = make_car('subaru', 'outback', color='blue', tow_packagge=True)
# print(car)



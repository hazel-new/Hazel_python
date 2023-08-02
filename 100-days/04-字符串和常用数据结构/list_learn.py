# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# append()
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# insert()
# motorcycles.insert(1, 'ducati')
# print(motorcycles)

# del
# del motorcycles[2]
# print(motorcycles)

# pop()
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# remove()
# motorcycles.remove('ducati')
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me.")

# practice1
# list_name = ['Tom', 'Jerry', 'Cat']
# # print(list_name)
# # print('Will invite ' + list_name[0] + ' and ' + list_name[1] + ' and ' + list_name[2] + ' to have supper!')
# print("Dear " + list_name[0]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[1]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[2]+":" + 'Could you please have supper with me?')
# print('\nCat cannot join the supper!')
#
# list_name.remove('Cat')
# # print(list_name)
# list_name.append('Dog')
# # print(list_name)
#
# print("\nDear " + list_name[0]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[1]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[2]+":" + 'Could you please have supper with me?')
#
# print("\nI found a more larger table!")
# list_name.insert(0, 'Bird')
# list_name.insert(2, 'Fox')
# list_name.append('Tiger')
# # print(list_name)
# print("\nDear " + list_name[0]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[1]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[2]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[3]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[4]+":" + 'Could you please have supper with me?')
# print("Dear " + list_name[5]+":" + 'Could you please have supper with me?')
#
# print("\nSorry, new table can't arrive on time and we just can invite 2 guests!")
#
# print("\nSorry, " + list_name[5] + " we can't invite you today!")
# list_name.pop(5)
# print("Sorry, " + list_name[4] + " we can't invite you today!")
# list_name.pop(4)
# print("Sorry, " + list_name[3] + " we can't invite you today!")
# list_name.pop(3)
# print("Sorry, " + list_name[2] + " we can't invite you today!")
# list_name.pop(2)
#
# print(list_name)
# print("\nDear " + list_name[0] + ": You still in the invite list!")
# print("Dear " + list_name[1] + ": You still in the invite list!")
#
# del list_name[0]
# print(list_name)
# del list_name[1]
# print(list_name)


# cars = ['bmw', 'audi', 'toyota', 'subaru']

# sort()
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# sorted()
# print(sorted(cars))
# print(sorted(cars, reverse=True))
# print(cars)

# reversed()
# cars.reverse()
# print(cars)

# len()
# print(len(cars))

# practice2
places = ['Norway', 'Sweden', 'Denmark', 'America', 'Britain']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))

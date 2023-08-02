def cities(city, country, population=''):
    if population:
        city_info = city.title() + "," + country.title() + " - population " + str(population)
    else:
        city_info = city.title() + "," + country.title()
    return city_info


# print(cities('shanghai', 'china', 10000))

def print_valid_cities(all_cities, used_cities):
   cities_different = all_cities.difference(used_cities)
   for city in cities_different:
        print(city)

all_cities = {
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан' , 'Новосибирск'}

print_valid_cities(all_cities, used_cities)
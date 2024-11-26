DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for name in DATABASE:
            friends_string += name + ' '
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        cities = set(DATABASE.values())
        friends_city = ''
        for city in cities:
            friends_city += city + ' '
        return 'Твои друзья в городах: ' + friends_city
    else:
        return '<неизвестный запрос>'
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

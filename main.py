''' 1 '''

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код

my_favorite_movies_list = my_favorite_movies.split(',')

print(my_favorite_movies_list[0])
print(my_favorite_movies_list[-1])
print(my_favorite_movies_list[1])
print(my_favorite_movies_list[-2])
# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Находим уникальные значения и создаем словарь для кодирования
unique_values = list(set(lst))
encoding = {value: [1 if value == val else 0 for val in unique_values] for value in unique_values}

# Преобразование в one hot encoding
one_hot_encoded = [encoding[value] for value in lst]

# Вывод результатов
for value, encoded in zip(lst[:5], one_hot_encoded[:5]):
    print(f'{value}: {encoded}')

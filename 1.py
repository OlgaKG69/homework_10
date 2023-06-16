# Задача 44:  В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst}) data.head()

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = [['robot'] for _ in range(10)] + [['human'] for _ in range(10)]

unique_values = list(set(item for sublist in data for item in sublist))

one_hot_data = []

for row in data:
    row_encoding = []
    for value in unique_values:
        if row[0] == value:
            row_encoding.append(1)
        else:
            row_encoding.append(0)
    one_hot_data.append(row_encoding)

for row in one_hot_data:
    print(row)

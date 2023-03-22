# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

my_list = [random.randint(-10, 10) for _ in range(20)]
print(my_list)

min_number = int(input('Enter the min value: '))
max_number = int(input('Enter the max value: '))

for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(i, end=', ')
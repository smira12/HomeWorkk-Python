# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.

import random


number = int(input('Input number of coins: '))
count_eagle = 0
count_tails = 0

for i in range(number):
    x = random.randint(0, 1)
    if x == 0:
        count_eagle += 1
    else:
        count_tails += 1
    print(x, end = ', ')
if count_tails > count_eagle:
    print('\n', count_eagle)
else:
    print('\n', count_tails)
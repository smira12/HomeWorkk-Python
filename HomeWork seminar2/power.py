# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.


n = int(input('Input number N: '))
i = 0
for i in range(n):
    if 2 ** i <= n:
        print(2 ** i, end = ' ')
        i += 1
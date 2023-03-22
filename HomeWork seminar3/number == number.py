# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

my_list1 = [random.randint(0, 100) for _ in range(30)]
print(my_list1)
number = int(input('Введите искомое число: '))

n = 0
closest = 0
min_d = max(my_list1) - number
if number in my_list1:
    for i in my_list1:
        if i == number:
            n += 1
    print(f'Число {number} встречается {n} раз')
else:
    for i in (my_list1):
        if abs(i - number) < min_d:
            min_d = abs(i - number)
            closest = i
    print(f'Введенное число {number} отсутствует Максимально близкое число {closest}')
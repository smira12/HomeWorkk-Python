# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки
from random import randint


bushes = list(randint(1, 20)for _ in range(int(input('Введите кол-во кустов: '))))
print(bushes)

number_bush = int(input('Введите № куста: '))
count = list()

if number_bush == 1:
    count = bushes[-1] + bushes[0] + bushes[1]
elif number_bush == len(bushes):
    count = bushes[-2] + bushes[-1] + bushes[0]
else:
    count = bushes[number_bush - 2] + bushes[number_bush - 1] + bushes[number_bush]
print(count)
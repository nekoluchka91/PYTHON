# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причем X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# x = 34; y = -30 -> 4

x = int(input('Введите координату X точки: '))
y = int(input('Введите координату Y точки: '))
if (x > 0 and y > 0):
    print('Первая четверть')
if (x < 0 and y > 0):
    print('Вторая четверть')
if (x < 0 and y < 0):
    print('Третья четверть')
if (x > 0 and y < 0):
    print('Четвертая четверть')
else:
    print('Неверно заданы координаты')
# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

a1 = int(input('Введите координату первой точки: ')) # 3
b1 = int(input('Введите координату первой точки: ')) # 6

a2 = int(input('Введите координату второй точки: ')) # 2
b2 = int(input('Введите координату второй точки: ')) # 1

result1 = (a2-a1)*(a2-a1)
result2 = (b2-b1)*(b2-b1)
result3 = round((result1+result2)**(1/2), 2)
print(result3)
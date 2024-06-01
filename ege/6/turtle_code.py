from turtle import *

tracer(0)  # чтобы сразу увидеть результат
left(90)  # поворачиваем в начальное положение

# рисуем фигуру
k = 40
for i in range(7):
    forward(10 * k)
    right(120)

# рисуем точки
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)

done()  # чтобы рисунок не закрывался

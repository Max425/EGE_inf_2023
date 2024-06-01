import turtle  # задание 15318

turtle.tracer(0)  # чтобы сразу увидеть результат
turtle.left(90)  # поворачиваем в начальное положение

# рисуем фигуру
k = 20
for i in range(2):
    turtle.forward(13 * k)
    turtle.right(90)
    turtle.forward(18 * k)
    turtle.right(90)

turtle.penup()

turtle.forward(5 * k)
turtle.right(90)
turtle.forward(9 * k)
turtle.left(90)

turtle.pendown()

for i in range(2):
    turtle.forward(11 * k)
    turtle.right(90)
    turtle.forward(7 * k)
    turtle.right(90)

# рисуем точки
turtle.pu()
for x in range(-k, k):
    for y in range(-k, k):
        turtle.goto(x * k, y * k)
        turtle.dot(5)

turtle.done()  # чтобы рисунок не закрывался

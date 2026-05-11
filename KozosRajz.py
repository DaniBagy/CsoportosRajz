#kozlekedesi lampa,alapja

import turtle

turtle.speed(0)
turtle.width(5)

i=0
while i <4 :
    turtle.color("grey")

    i += 1

szog = 90
hossz = 50

i = 0
while i < 3:
    if i == 0:
        turtle.color("green")
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.setheading(szog)
    elif i == 1:
        turtle.color("yellow")
        turtle.penup()
        turtle.goto(0, 125)
        turtle.pendown()
        turtle.setheading(szog)
    else:
        turtle.color("red")
        turtle.penup()
        turtle.goto(0, 250)
        turtle.pendown()
        turtle.setheading(szog)

    c = 0
    while c < 180:
        turtle.forward(hossz)
        turtle.right(szog + szog + 1)
        turtle.forward(hossz)

        c += 1

    i += 1
turtle.done()
#kozlekedesi lampa,alapja

import turtle

turtle.speed(0)
turtle.width(5)
hossz = 25
szog = 90
i=0
turtle.begin_fill()
while i <2 :
    turtle.color("grey")
    turtle.forward(hossz)
    turtle.right(szog)
    turtle.forward(hossz * 12)
    turtle.right(szog)
    turtle.forward(hossz)
    i+=1
turtle.end_fill()
hossz = 75
j=0
turtle.begin_fill()
while j< 2:
    turtle.color("black")
    turtle.forward(hossz)
    turtle.left(szog)
    turtle.forward(hossz*4)
    turtle.left(szog)
    turtle.forward(hossz)

    j+=1
turtle.end_fill()

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
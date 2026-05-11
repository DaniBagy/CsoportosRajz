#kozlekedesi lampa,alapja

import turtle

turtle.speed(5)
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
turtle.done()
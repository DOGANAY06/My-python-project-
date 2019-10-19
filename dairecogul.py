import turtle
import random
t=turtle.Turtle(shape="turtle")
renk=["pink","blue","yellow","purple","orange"]
t.speed(100)
while True:
    kac=int(turtle.numinput("Kaç adet daire olsun","cevap ver"))
    turtle.bgcolor("white")
    for x in range (kac):
        t.pensize(15)
        t.pencolor(random.choice(renk))
        t.circle(50)
        t.left(360/kac)

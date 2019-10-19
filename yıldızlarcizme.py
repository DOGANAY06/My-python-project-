import turtle
import random 
turtle.bgcolor("black")
turtle.pencolor("yellow")
def yildizciz(x,y):
    boyut=random.randint(1,49)
    turtle.penup ()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("red") #dolgu rengini belirle
    turtle.begin_fill()
    for x in range(5):
        turtle.fd(boyut)    
        turtle.right(120)
        turtle.fd(boyut)
        turtle.left(50)
    turtle.end_fill()    
turtle.onscreenclick(yildizciz) #ekrana tıkladığında yıldız cizen parametre

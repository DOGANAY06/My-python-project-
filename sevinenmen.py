import turtle 
t=turtle.Pen()
t.speed(10)
turtle.bgcolor("yellow")
def sevinen(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    #yüz için 
    t.pencolor("pink")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #sol göz için
    t.setpos(x-15,y+60)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #sag göz için 
    t.setpos(x+15,y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #agiz 
    t.setpos(x-20,y+10)
    t.pencolor("orange")
    t.width(10)
    t.goto(x-20,y+5)
    t.goto(x+10,y-10)
    t.goto(x+20,y+10)
    t.width(1)
turtle.onscreenclick(sevinen)

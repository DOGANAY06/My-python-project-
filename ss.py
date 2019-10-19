import turtle 
turtle.pensize(9)
def ileri():
    turtle.fd(100)
def geri():
    turtle.backward(100)
def sol():
    turtle.left(90)
def sag():
    turtle.right(90)
def pink():
    turtle.pencolor("pink")
def speed():
    turtle.speed(10)
def time():
    turtle.time(10)
turtle.onkeypress(ileri,"Up")
turtle.onkeypress(geri,"Down")
turtle.onkeypress(sol,"Left")
turtle.onkeypress(sag,"Right")
turtle.onkeypress(pink,"p")
turtle.onkeypress(speed,"n")
turtle.onkeypress(time,"t")
turtle.listen()

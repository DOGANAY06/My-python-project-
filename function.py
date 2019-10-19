# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:22:52 2019

@author: Doğan AY
"""
import turtle 
turtle.bgcolor("yellow")
turtle.pensize(5)
def heart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
turtle.speed(0)
turtle.color("black","red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111,65)
heart()
turtle.left(120)
heart()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
#%%
import turtle 
def halka (x,y,renk):
    turtle.pensize(10)
    turtle.pencolor(renk)
    turtle.penup() #kalemi kaldır
    turtle.goto(x,y)
    turtle.pendown()  #kalemi bastır
    turtle.circle(100)
halka(-200,50,"red")
halka(-50,50,"black")
halka(100,50,"yellow")
halka(-125,-25,"blue")
halka(25,-25,"green")
#%%
def fonksiyon():
    print("Hi")
    print("How are you")
    print("What's up")
fonksiyon()
#%%
import turtle 
def karem():
    turtle.home()   #merkezze getirmek için parametresiz bir fonksiyondur
    for x in range(4):  #4 kere bu cizimi tekrarladık
        turtle.fd(100)   
        turtle.left(90)
karem()
#%%
import turtle 
def karem(renk):
    turtle.home()
    turtle.pencolor(renk)
    for x in range(4):
        turtle.fd(100)
        turtle.left(90)
kullanicirenk=input("Rengi giriniz")
karem(kullanicirenk)
#%%
import turtle 
def kare(renk,genislik): #değiştirmek istediğimiz parametreleri girdik bu sayede 
    turtle.home()
    turtle.pencolor(renk)
    for x in range (4):
        turtle.fd(genislik)
        turtle.left(90)
kullanicirenk=input("Ne renk olsun=")
kullanicigenislik=int(input("Kaç cm'lik kare cizmek istersiniz="))
kare(kullanicirenk,kullanicigenislik) 
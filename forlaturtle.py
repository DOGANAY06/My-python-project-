# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:54:23 2019

@author: Doğan AY
"""

import turtle
turtle.color("green")
turtle.bgcolor("yellow")
for x in range(4):
    turtle.write("x:"+str(x))
    turtle.fd(100)
    turtle.left(90)
#%% daire cizme 
import turtle 
turtle.color("white")
turtle.bgcolor("red")
turtle.home()   #başlangıç noktasına git 
turtle.pensize(10)
for x in range (360): 
    turtle.fd(1)    
    turtle.left(1)
#%%
import turtle
turtle.color("yellow")
turtle.bgcolor("red")
turtle.pensize(5)
for x in range (36): #36 adet iç içe kare yap 
    turtle.home()    #merkeze git 
    turtle.left(x*10)   # 10,20,30....350 dereceye kadar sola dön
    turtle.circle(100)   #100 yarı çaplı daire ciz
#%%
import turtle
turtle.color("red")
turtle.bgcolor("yellow")
for x in range (200):
    turtle.fd(x)
    turtle.left(91)
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 01:04:57 2019

@author: Doğan AY
"""

import turtle 
renkler=["brown","black","yellow","orange"]
turtle.pensize(2)
turtle.home()
turtle.speed(5)
for x in range (200):
    siradakirenkindexi=x%4 
    siradakirenk=renkler[siradakirenkindexi]
    turtle.pencolor(siradakirenk)
    turtle.forward(x)
    turtle.left(91)
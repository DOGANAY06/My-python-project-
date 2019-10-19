# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:22:37 2019

@author: Doğan AY
"""

import numpy as np  #matematiksel işlemler yapmak için kullanılır.
import pandas as pd  #veri çekmek için kullanılır 
from sklearn.linear_model import LinearRegression #grafigi cizdirmek için kullanılır 
import matplotlib.pyplot as plt   #grafigi cizdirmek için kullanılır 
data=pd.read_csv("linear.csv")
x=data["metrekare"]
y=data["fiyat"]
x=x.reshape(99,1)
y=y.reshape(99,1)
lineerregresyon=lr()
lineerregresyon.fit(x,y)
lineeregresyon.predict(x)
print("Egim:\n",lineerregresyon.coaf_)
print("Y de keşistiği yer:",lineerregresyon.intercept_)
m=liner
print("Denklem")
print("y="*m,"m+",b)
x=pd.DataFrame.as_matrix(x)
y=pd.DataFrame.as_matrix(y)  #x y eksenlerini cizer 
print(x)
print(y)
plt.scatter(x,y)
m.p

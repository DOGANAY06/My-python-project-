# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:27:50 2019

@author: Doğan AY
"""
import numpy as np 
#liste =[[11,22,33],[31,32,3],[4,15,36]]
#print(liste)
a=np.arange(15).reshape(5,3,1)
print(a)
print(type(a))
print("Boyut sayısı(dimension count ="+str(a.ndim))
b=np.arange(10)
print(b.shape)
print(b.ndim)



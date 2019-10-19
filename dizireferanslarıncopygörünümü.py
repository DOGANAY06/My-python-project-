# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:09:15 2019

@author: Doğan AY
"""
import numpy as np 
a=np.arange(10)
print(a)
b=a
print(b)
b[0]=100
print(a)
print(b)
c=a.copy() 
print(c)
c[0]=1000
print(a)
print(c)
#%%
a=np.arange(6)
b=a.view()
print(a)
print(b)
b[0]=1000
print(a)
print(b)
b.shape=2,3
print(b)
print(a)
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:21:12 2019

@author: Doğan AY
"""

a=[10,11,12,13,14]
b=[]
for i in a :
    b.append(i**2)
print(b)
#%%
def fonksiyon(i):
    return i**3 + i**2 +i+1
print(b)
#%%
a=[1,2,3,4,5]
b=[fonksiyon(i)for i in a ]
print(b)
#%%
b= []
for x in [int(input("Sayıyı giriniz="))]:
    for y in [x,2,3]:
        b.append(x*y)
print(b)
#%%
a=[1,2,3,4,5]
b=[]
for i in a :
    if i%2==1:
        b.append(i)
print("Bunlar tek sayıdır",b)

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:50:31 2019

@author: Doğan AY
"""

a=[1,2,3,4]
a_iter=iter(a)
print(next(a_iter))
#%%
a=[12,15,19,24]
a_iter=iter(a)
while True:
    try:
        element=next(a_iter)
        print(element)
    except StopIteration:
        print("Hatalı döngü dönüsü")
        break
#%%
gerisayim=60
rakamlar=gerisayim
myiter=iter(rakamlar)
for x in myiter:
    print(x)
#%%
rakamlar=gerisayim(60)
myiter=iter(rakamlar)
next(myiter)
[i for i in myiter]
print(myiter)
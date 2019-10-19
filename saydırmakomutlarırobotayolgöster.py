# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 00:01:29 2019

@author: Doğan AY
"""

for counter,meyve in enumerate(["elma","armut","muz"]):
    print("{} - {}".format(counter,meyve))
#%%
for counter,job in enumerate(["markete git","meyve al","sebze al","et al","eve git","yemegi hazırla"],1):
    print("{}-{}".format(counter,job))
#%%
def teksayi(x):
    return x%2==1
a=[10,12,1231212,1241224,25345123,4552231]
b=list(filter(teksayi,a))
print(b)
#%%
def ciftsayi(x):
    return x%2==0
a=[1012,123123231,1242323412,523512312,534431]
b=list(filter(ciftsayi,a))
print(b)
#%%

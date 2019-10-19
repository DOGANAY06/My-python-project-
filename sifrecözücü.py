# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:31:59 2019

@author: Doğan AY
"""

rakamlar="0123456789"
sayac=0
for a in rakamlar:
    for b in rakamlar:
        for c in rakamlar :
            sayac=sayac+1
            sifre=a+b+c
            print(sifre)
print("toplam",sayac,"adım")
#%%
buyuk="QWERTYUIOPASDFGHJKLZXCVBNM"
kucuk="qwertyuiopasdfghjklxcvbnm"
rakamlar="0123456789"
sayac=0
for a in buyuk :
    for b in  kucuk:
        for c in rakamlar:
            sayac=sayac+1
            sifre=a+b+c or b+c+a or c+b+a or c+a+b
            print(sifre)
print("toplam",sayac,"adım")
#%%
rakamlar="0123456789"
sayac=0
for a in rakamlar :
    for b in rakamlar:
        for c in rakamlar:
            for d in rakamlar:
                for e in rakamlar:
                    for f in rakamlar:
                        sayac=sayac+1
                        sifre=a+b+c+d+e+f or b+a+c+d+e+f or c+a+b+d+e+f or d+a+b+c+e+f or e+a+b+c+d+f or f+a+b+c+d+e 
                        print(sifre)
print("topkam",sayac,"adım da cözüldü")
#%%

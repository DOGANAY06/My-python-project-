# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:27:21 2019

@author: Doğan AY
"""

sayi=int(input("Sayıyı giriniz asal mı kontrol edelim ="))
x=1
while x<sayi:
    x+=1
    kalan=x%sayi
if kalan>=1:
    print("Sayı asaldır=")
else:
    print("Sayı asal değildir=")
#%%
sayi=int(input("Sayıyı giriniz asal mı kontrol edelim ="))
i=2
for i in range(sayi):
    sonuc=i%sayi
if sonuc>=1:
    print("Sayı asaldır=")
else:
    print("Sayı asal değildir=")
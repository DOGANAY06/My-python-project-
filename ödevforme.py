# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:13:19 2019

@author: Doğan AY
"""

sayi=int(input("Sayıyı giriniz="))
yuzler=int(sayi/100)
print("Yüzler basamagıdır=",yuzler)
onlar=int(sayi/10)%10
print("Onlar basamagıdır=",onlar)
birler=int(sayi%10)
print("Birler basamagıdır=",birler)
teachersaid=(yuzler**2)+(onlar**2)+(birler**2)
print("Her basamağın karesi ve toplamlar=",teachersaid)
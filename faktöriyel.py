# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:12:17 2019

@author: Doğan AY
"""

sayi=int(input("Lütfen faktoriyelini hesaplıcağınız sayıyı giriniz="))
faktoriyel=1
if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz=")
elif sayi>0:
    for i in range (1,sayi+1):
        faktoriyel=faktoriyel*i
    print(faktoriyel)
else:
    print("Sayı 0'dır=1")




















# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 00:26:19 2019

@author: Doğan AY
"""
sayi=int(input("Asal mı ? "))
for asal in range (2,sayi):
    if sayi%asal==0:
        print("Sayı asal değildir")
        break
    else:
        print("Sayı asaldır")
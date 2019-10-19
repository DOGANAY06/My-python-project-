# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 01:51:53 2019

@author: Doğan AY
"""

import random 
sayi=random.randint(1,49)
hak=1
user=int(input("Sayıyı giriniz="))
while 6<=hak:
    hak=hak+1
    user=hak
if sayi==user:
    print("Doğru sayıyı buldunuz")
else:
    print("Tekrar deneyiniz=",sayi)
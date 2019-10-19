# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:53:59 2019

@author: Doğan AY
"""

import time 
import sys
print("Bomba kuruldu çabuk sifreyi gir..!")
time.sleep(4)
sifre=int(input("Sifreyi giriniz="))
print("Sifre doğru mu kontrol ediliyor")
for i in range(5,0,-1):
    time.sleep(1)
    print(i) 
if sifre==19980658  :
        print("Bomba durduruldu.")
else:
        print("Bomba patladı")
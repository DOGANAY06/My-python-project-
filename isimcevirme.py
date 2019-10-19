# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:24:27 2019

@author: Doğan AY
"""

def terscevir(metin):
    tershali=metin[::-1] #metni tam ters cevirir tek başına 
    return tershali
cumle=str(input("Metni giriniz="))
print(terscevir(cumle))
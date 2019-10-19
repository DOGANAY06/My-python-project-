# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:26:20 2019

@author: Doğan AY
"""

sozluk={
        "Günaydın":"Good Morning",
        "İyi Akşamlar":"Good Evening",
        "Merhaba":"Hello"
        }
silinecek=input("Lütfen silinecek kelimeyi giriniz=")
if silinecek in sozluk.keys():
    sozluk.pop(silinecek)
    print("Silindi",sozluk)
else:
    print("Silinme işlemi başarısız")
#%%
onemlino={
        "155":"Polis",
        "110":"İtfaiye",
        "112":"Ambulans",
        "156":"Jandarma",
        "154":"Trafik Polisi"}
anahtar=input("Lütfen Aradığınız numarayı yazınız=")
if anahtar in onemlino.keys():
    deger=onemlino[anahtar]
    print(deger)
else:
    print("Böyle bir numara yok")

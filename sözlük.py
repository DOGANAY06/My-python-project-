# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:02:20 2019

@author: Doğan AY
"""

sozluk={"scissors":"makas","book":"kitap"}

print(sozluk["scissors"])
sozluk["book"]="rezervasyon yapmak"
print(sozluk)
sozluk2=dict(makas="scissors",kitap="book")
print(sozluk2)
del(sozluk["book"])
print(sozluk)
print(len(sozluk))
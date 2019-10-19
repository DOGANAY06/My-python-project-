# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 00:19:21 2019

@author: Doğan AY
"""

from datetime import date 
class Kitap:
    def __init__(self,yazar:str,isim:str,basimtarihi:date,page:int):
        self.yazar=yazar
        self.isim=isim
        self.basimtarihi=basimtarihi
        self.page=page
x=Kitap("Doğan AY","Kodlamaya giriş",date(2013,3,8),240)
print(x.isim)
print(x.basimtarihi.day)
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:07:41 2019

@author: Doğan AY
"""

cinsiyet=input("Cinsiyetinizi Giriniz [erkek/kız]=")
yas=int(input("Yaşınızı Giriniz="))
if cinsiyet=="erkek" and yas>=20:
    print("Askere gelebilirsiniz")
elif  cinsiyet=="erkek" and yas<=20:
    print("Yaşınız tutmuyor")
else:
    print("Cinsiyetiniz ve yaşınız uygun değildir")
#%%
yas=int(input("Yaşınızı giriniz="))
if (yas<=9 or yas>=65):
    print("Ücretsiz biniş")
elif yas>=10 and yas<=30 :
    print("İndirimli kart")
else:
    print("Normal Kart")
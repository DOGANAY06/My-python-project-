# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:39:03 2019

@author: Doğan AY
"""

sifre=input("Şifrenizi giriniz=")
buyuk="ABCDEFGHIJKLMNOPRSTVYZ" #büyük harf listesi
kucuk="abcdefghijklmnoprstvyz"  #kücük harf listesi
digit="0123456789"   #sayı listesi çünkü en az 1 sayı olmalıydı
bhsayi=0               #kaç tane büyük kücük sayi oldugunu istedk 0 verdik başlangıçta
khsayi=0
dsayi=0
for harf in sifre:     # sifredeki her bir harf için 
    if harf in buyuk:  #eger büyük hatf ise verdiğimiz 0 ı bir artır 
        bhsayi=bhsayi+1 #kontrol ettik harf değişkenin içindeki büyük küçük sayıyı 
    if harf in kucuk:
        khsayi=khsayi+1
    if harf in digit:
        dsayi=dsayi+1
if (bhsayi==0) or (khsayi==0) or (dsayi==0) or (len(sifre)<8): #eger istediğimiz seyler yoksa sifre güvensizdir yazdır 
    print("Sifreniz güvenli değildir.")
else:
    print("Sifreniz onaylanmıştır.")
#%%
import turtle
turtle.speed(10) 
turtle.bgcolor("red")
turtle.color("yellow")
for x in range(28):
    turtle.left(10)
    if (x%2==0):
        turtle.begin_fill()
    for y in range (3):
        turtle.fd(100)
        turtle.left(120)
        turtle.write(x)
    turtle.end_fill()
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:25:25 2019

@author: Doğan AY
"""

import os 
dir(os)
#%%
import speech
import time
response = speech.input("Say something, please.")
speech.say("You said " + response)

def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    speech.say(phrase)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)
#%%
import os 
os.name
if os.name=="nt":
    print("Windows sizin isletim sisteminiz")
else:
    print("Başka birşey")
#%%
liste=["a","b","c","d","e"]
import random 
random.choice(liste)
random.randint(1,5)
#%%
import random 
a=random.randint(1,7)
sayac=3
for i in range (0,5):
    print(i,".")
    sayi=int(input("Sayı giriniz="))
    if sayi > a:
        print("Sayıdan büyüksünüz=")
        sayac=sayac+1
    elif sayi==a:
        print("Tebrikler =")
        sayac=sayac+1
        break
    elif sayi<a:
        print("Sayı dan kücüksünüz =" )
        sayac=sayac+1
else:
    print("Sayıyı bilemediniz=",a) #break komutundan sonraki else for elseyi ifade eder ve for la aynı hizada olmalı 
#%%
a=random.randint(1,100)
hak=3
while True:
    sayi=int(input("Sayıyı giriniz:"))
    if (sayi<a):
        print("Sayıyı giriniz...")
        hak=hak-1
    elif sayi>a:
        print("Daha düsük bir sayi söyleyin")
        hak=hak-1
    else:
        print("Tebrikler! Sayımız",a)
        break
    if (hak==0):
        print("Hakkınız bitti...")
        print("Sayımız:",a)
        break
#%%
import datetime
gecerlizaman=datetime.datetime.now() #şuanki zamanı yazarız
print(gecerlizaman)
#%%
print("Şuanki zaman",gecerlizaman)   
print("Year:",end="") 
print(gecerlizaman.year)
print(gecerlizaman.month)
print(gecerlizaman.hour)
print(gecerlizaman.second)
print("Minute:",end ="")
print(gecerlizaman.minute)
#%%
zaman="2019-09-29"
print("Zamanın kaldı=",zaman-gecerlizaman)
#%%
#fibonacci sayısı ödev 
def Topla(sayi1,sayi2):  #fonksiyon tanımlamak  için kullanılır 
    print(sayi1+sayi2) 
Topla(3,5)  
sy1=int(input("Sayı girinz=")) #sayı girdisini alın sayıları toplatın 
sy2=int(input("Sayıyı giriniz="))
Topla(sy1,sy2)
#%%
x=int(input("Sınav notunuz:"))
def sinavdegerlendirme(sinavnot):
    if sinavnot>100 or sinavnot<0:
        print("Hatalı girdin:")
    else:
        if sinavnot>50:
            print("Gectin")
        else:
            print("Sınavda kaldın")
sinavdegerlendirme(x)
#%%
name1=input("İsminizi ve soyisminizi  girinz:")
name2=input("Soyisiminizi  ve isminizi giriniz:")
print("Alfabetik  sıraya göre")
if name1<name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
#%% 153 sayısının sayılarının rakamlarının karesini alan program 
sayi=153
birlerbasamagı=3
onlarbasamafı
#%%
birds=int(input("Kuş sayısı giriniz="))
def main():
    texas()
    ankara()
def texas():
    birds=5000
    print('Texas has',birds,'birds')
def ankara():
    #birds=11000
    print('Ankara has got',birds,'birds')
main()
#%%

def main():
    first_name=input("İsminizi giriniz=")
    last_name=input("Soyadınızı giriniz=")
    print("Reezervasyon iŞlemi sahibi")
    reverse_name(first_name,last_name)
def reverse_name(first,last):
    x=last
    y=first
    print(last,first)
    print(y,x)
main()
#%%
def main():
    value=int(input("Sayıyı giriniz="))
    show_double(value)
def __init__show_double(value): # buna başka  bir değişkende girebiliriz fonksiyonlar için 
    result =value * 2 
    print(result)
main()
#%%
highscore=50
def main():
    test1=int(input("1.Sınav notunu giriniz="))
    test2=int(input("2.Sınavı giriiz="))
    test3=int(input("3.SINAVI GİRİNİZ="))
    average=(test1++test2+test3)/3
    print("Ortalama=",average)
def hesaplama(average):  
    if average>=highscore:
        print("tEBRİKLER")
main()
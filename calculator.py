# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:00:49 2019

@author: Doğan AY
"""

def toplam(sayi1,sayi2):
    return (sayi1+sayi2)
def cikarma(sayi1,sayi2):
    return (sayi1-sayi2)
def carpma(sayi1,sayi2):
    return (sayi1*sayi2)
def bolme(sayi1,sayi2):
    return (sayi1/sayi2)
print("Toplama:1")
print("Çıkarma:2")
print("Çarpma:3")
print("Bölme:4")
secenek=input("İşlem seciniz=")
sayi1=int(input("1.Sayıyı giriniz="))
sayi2=int(input("2.sayıyı giriniz="))
if secenek=='1':
    print("Toplam="+str(toplam(sayi1,sayi2)))
elif secenek=='2':
    print("Çıkarma="+str(cikarma(sayi1,sayi2)))
elif secenek=='3':
    print("Çarpma sonucu="+str(carpma(sayi1,sayi2)))
elif secenek=='4':
    print("Bölümü="+str(bolme(sayi1,sayi2)))
else:
    print("Geçersiz işlem secildi")
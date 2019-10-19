# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:33:20 2019

@author: Doğan AY
"""

def sifrele(metin):
    sifrelimetin=""
    for harf in metin:
        asciikod=ord(harf)
        asciikod=asciikod+3
        karakterkod=chr(asciikod)
        sifrelimetin=sifrelimetin+karakterkod
    f=open("dnyadatrkedebiyat_20150706114949014.txt","a")
    f.write(sifrelimetin)
    f.close()
    print("dosyayı kaydettim=")
def sifrecoz():
    sifresizmetin=""
    metin=""
    f=open("dnyadatrkedebiyat_20150706114949014.txt","r")
    metin=f.read()
    for harf in metin:
        asciikod=ord(harf)
        asciikod=asciikod-3
        karakterkod=chr(asciikod)
        sifresizmetin=sifresizmetin+karakterkod
    print("Şifreli",metin,"Şifresiz:",sifresizmetin)
 
sifrele(sifrele)
sifrecoz()

    
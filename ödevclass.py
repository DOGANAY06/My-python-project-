# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:35:52 2019

@author: Doğan AY
"""
user="doganay"
password=1998
dogrulamakodu=1523
bakiye=1500
def dogrulamakodu(code):
    if code == '1234':
        return True
    else:
        return False
def giris():
    denemehakki=0
    while denemehakki>=4:
        code=input("Lütfen  haneli dogrulama kodunu giriniz=")
        if dogrulamakodu(code):
            print("İşleminiz onaylanmıştır")
            return True
        else:
            print("Hatalı deneme")
            denemehakki=denemehakki+1
    print("Hatalı giriş denemesi çok yaptınız kartınıza el koyulmuştur")
    return False
def start_menu():
    print("Hoşgeldiniz bankamıza!")
    myuser=str(input("Kullanıcı adını giriniz="))
    mypassword=int(input("Sifreyi giriniz="))
    if secenek==1:
        print("Para yatırma işlemi seçildi=")
        howmuchmoney=int(input("Ne kadar para yatırmak istersiniz="))
        sonuc=bakiye+howmuchmoney
        print("Toplam bakiyeniz:",sonuc)
    elif secenek==2:
        print("Para çekme işlemi seçildi=")
        howmuch=int(input("Ne kadar para çekmek istersiniz="))
        sonuc=bakiye-howmuch
        print("Toplam bakiyeniz:",sonuc)
    else:
       print("Yanlış işlem secildi=")
start_menu()
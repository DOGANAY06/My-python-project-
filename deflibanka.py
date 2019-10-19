# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:25:22 2019

@author: Doğan AY
"""

myuser="doganay"
mypassword=1998
bakiye=19226
mycode=1563
p=0.6
z=0.2
def parayatir():
    x=int(input("Ne kadar yatırmak istersiniz="))  #üsteki fonksiyonlar dışarıda tanımlanır buna göre def main altında yapacagımız işlemieri yazarız 
    sonuc=bakiye+x
    print("Total money=",sonuc)
def paracek():
    x=int(input("Ne kadar para çekmek istersiniz="))
    sonuc=bakiye-x
    print("Total money=",sonuc)
def faiz():
    ay=int(input("Kaç aylık yatırmak istersiniz="))
    sonuc=bakiye*ay*p*z
    print("Faiz ve vergi girildikten sonraki hali =",sonuc)
def main():
    user=str(input("Kullanıcı adınızı giriniz="))
    password=int(input("Sifrenizi giriniz="))
    code=int(input("Kodunuzu giriniz="))
    if myuser==user and mypassword==password and  mycode==code :
        print("Doğan bey hoşgeldiniz=")
        secenek=int(input("Para yatırmak için {1} Para cek {2}Faiz {3} Vergi {4}="))
        if secenek ==1:
            parayatir()
        elif secenek==2:
            paracek()
        elif secenek==3:
            faiz()
        else:
            print("Hatalı giriş yaptınız=")
    else:
        print("Hatalı giriş yapıldı=")
main()
        
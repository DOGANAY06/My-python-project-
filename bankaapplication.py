# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:42:22 2019

@author: Doğan AY
"""
from time import sleep
from os import system 
class Musteri:
    def __init__(self,soyIsim:str,Idno:str,Tcno:str,Parola:str):
        self.__soyIsim=soyIsim
        self.__Idno=Idno
        self.__Tcno=Tcno
        self.__Parola=Parola
        self.__bakiye=0
    def getsoyIsım(self): #ulaşılabilir metotlardır get'le tanımlanan self ler 
        return self.__soyIsim
    def getIdno(self):
        return self.__idno
    def getTcno(self):
        return self.__tcno
    def getParola(self):
        return self.__parola
    def getBakiye(self):
       return self.__bakiye
    def setBakiye(self,miktar:float):
        self.__bakiye=miktar 
class Banka :
    def __init__(self,isim:str):
        self.__isim=isim
        self.__musteriler=list()
    def  musteriVarmi(self,Tcno:str,Parola:str):
        for i in self.__musteriler:
            if i.getTcno()==Tcno and i.getParola()==Parola : #girilen paramaetrelerin doğrulugu kontrol edilir.
                return i #müsteri kontrolü yapmak için vardır 
        return False # return i çalışmayınca  buna gider çünkü öyle bir müsteri yokturdur.
    def aliciVarmi(self,Idno):
        for i in self.__musteriler:
            if i.getIdno ()==Idno :
                return i 
        return False 
    def paraAktar (self,gonderen:Musteri,alici:Musteri,miktar:float) :#para aktarımı için gerekli paramaetreyi yazdık 
        if gonderen in self.__musteriler and alici in self.__musteriler:
            if gonderen.getBakiye()>=miktar:
                gonderen.setBakiye(gonderen.getBakiye()-miktar)
                alici.setBakiye(alici.getBakiye()+miktar)
                print("Para gönderimi başarılı")
            else:
                print("Para gönderimi başarısız,başka işlemi deneyiniz")
        else:
            print("Alıcı hesap numarası tanımlanamadı")
    def musteriOl(self,soyIsım:str,Idno:str,Tcno:str,Parola:str):
        self.__musterier.append(Musteri(soyIsim,Idno,Tcno,Parola))
    def paraCek(self,musteri:Musteri,miktar:int):
        if miktar % 5 !=0:
            print("Paranız 5'in katları olması gerekiyor" )
        else:
            if musteri.getBakiye()>=miktar:
                print("Paranız hazırlanıyor hazneden teslim alınız" )
                musteri.setBakiye(musteri.getBakiye()-miktar)
            else:
                print("Bakiye yetersiz ")
    def parayatir(self,musteri:Musteri,miktar:int):
        if miktar %5 == 0:
            print("Paranızı hazneye yerleştiriniz")
            musteri.setBakiye(musteri+getBakiye()+miktar)
        else:
            print("Paranızı 5'in katları olacak şekilde hazneye yerleştirip paranızın sahte olup olmadığını kontrol ediniz")
    def bakiyebilgisi(self,musteri:Musteri):
        print("""
        Soyisim: \t {}
        Bakiye: \t {}
        """.format(musteri.getsoyIsım(),musteri.getBakiye()))
def main():
    banka=Banka("Güven Bank")
    while True:   #döngüden secim yapıcaz 
        system("cls") #terminal temizleme islemi 
        print ("""
        [1]  Musteri Ol 
        [2] Giriş Yap
         """)
        secim=str(input("Seciminizi yapınız ="))
        if secim=="1":
            soyIsım=str(input("Soyisminizi Giriniz="))
            Idno=str(input("Müsteri numarası giriniz ="))
            Tcno=str(input("T.C. kimlik numarasını giriniz ="))
            Parola=str(input("Uygulamak istediğiniz parolanızı giriniz="))
        elif secim=="2":
            soyIsim=str(input("Bankamıza kayıtlı soyisimi giriniz="))
            Idno=str(input("Belirlediğiniz müsteri numarasını giriniz  ="))
            Tcno=str(input("T.C. kimlik numarasını giriniz ="))
            Parola=str(input("Giriş yapmak için parolanızı giriniz="))
    if banka.musteriVarmi(Tcno,Parola):
        while True:
            system("cls")
            print("""
[1] Para aktar  *****     [2] Para cek 
[3]  Para yatır *****    [4] Bakiye Bilgisi 
              [ESC] Çıkış 
                      """)
            secim2=int(input("Seciminizi yapınız="))
            if secim2=="1":
                Idno=input("Alıcının hesap numarasını giriniz=")
                miktar=float(input("Göndermek istediğiniz tutarı giriniz ="))
                if banka.aliciVarmi(Idno):
                    banka.paraAktar(musteri,banka.aliciVarmi(Idno),miktar)
                else:
                    print("Alıcı tanımlanamadı")
            elif secim2=="2":
                miktar=input("Miktarı giriniz =")
                banka.paraCek(musteri,miktar)
                input("Ana menüye dönmek için 'enter' dokun")
            elif secim=="3":
                miktar=input("Miktarı giriniz=")
                banka.parayatir(musteri,miktar)
                input("Ana menüye dönmek için 'enter' dokun")
            elif secim=="4":
                banka.bakiyebilgisi(musteri)
                input("Ana menüye dönmek için 'enter' dokun")
            elif secim=="ESC":
                print("Çıkış yapılıyor,ana menüye yönlendiriliyorsunuz")
                sleep(10)
                break
            else:
                print("Hatalı giriş yaptınız")
                input("Menüden çıkmak için 'enter' a dokunun ")
if __name__=="__main__":
    main()
        
        
        
        
        
        
        
        
        
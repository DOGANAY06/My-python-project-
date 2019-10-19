# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:07:15 2019

@author: Doğan AY
"""
from os import system 
from random import randint 
class Silah:
    def __init__(self,isim,damage):
        self.__isim=isim
        self.__damage=damage
    def vur(self,rakip):
        rakip.setCan(rakip.getCan()-self.__damage) 
        self.__damage-=1
    def getIsim(self):
        return self.__isim
    def getDamage(self):
        return self.__damage
class Karakter:
    def __init__(self,can:int,silah:Silah):
        self.__can=can
        self.__silah=silah
    def vur(self,rakip):
            self.__silah.vur(rakip)
    def getCan(self):
        return self.__can
    def setCan(self,yeniCan:int):
        self.__can=yeniCan
    def getSilahIsim(self):
        return self.__silah.getIsim()
    def getDamage(self):
        return self.__silah.getDamage()

class Dusman(Karakter):
    pass
class Player(Karakter):
    def __init__(self,isim:str,can:int,silah:Silah):
        Karakter.__init__(self,can,silah)
        self.__isim=isim
    def getIsim(self):
        return self.__isim
def Main():
    dusmanlar=[]  #düsman değişkenini tanıyıp 10 tane düsman attık 
    for i in range(10): #öldürdükçe yeni canavar gelicek
        dusmanlar.append(Dusman(randint(30,50),Silah("Bıcak",randint(0,15))))  #düsmanın gücü ve silahı rastgele tanımladım 
    player=Player("Doğan",80,Silah("AKM",80))  #oyuncumuzun silahı ve güc 
    while True: 
        system("cls")  #ekrandaki canavarların yazmamasını istedik 
        print(" Oyuncu:{} ******* Can:{}******** Silah:{}******** Dost Damage:{}".format(player.getIsim(),player.getCan(),player.getSilahIsim(),player.getDamage()))
        print("*******************************")
        for sayi,i in enumerate (dusmanlar):
            print("No:{} ********Düsman Can:{} ******* Düsman Damage:{} ***********Düsman Silah:{}".format(sayi,i.getCan(),i.getDamage(),i.getSilahIsim()))
        print ("*****************************")
        secim=input("Saldırılacak olan düsmanı:")
        dusman=dusmanlar[int(secim)]
        player.vur(dusman)
        if dusman.getCan() <=0: #düsmanın canı 0 dan azsa 
            dusmanlar.remove(dusman) #düsmanı ortadan kaldır 
            if not  dusmanlar:  #düsman yoksa 
                print("Sen kazanadın") # oyunu kazandın 
                break
        if dusmanlar:
            dusmanlar[randint(0,len(dusmanlar)-1)].vur(player) #☺düsmanların vurması için oyuncuya bunu tanımladım 
            if player.getCan()<=0: #kullanıcının canı 0 dan azsa 
                print("Game Over You died") #kullanıcı kaybetti 
                break
if __name__=="__main__":
    Main()
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:05:21 2019

@author: Doğan AY
"""

class Dusman():
    def __init__(self):
        self.can=100
        self.guc=40
    def vur(self,oyuncu):
        oyuncu.can-=self.guc
class Oyuncu():
    def __init__(self):
        self.can=500
        self.guc=100
    def vur(self.dusman):
        dusman.can-=self.guc
player=Oyuncu()
player.can
player.guc
dusmanlar=[]

for i in range(10):
    dusmanlar.append(Dusman())
dusmanlar[0].can
player.vur(dusmanlar[3])

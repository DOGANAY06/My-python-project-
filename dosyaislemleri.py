# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:16:35 2019

@author: Doğan AY
"""

f=open("Yeni Metin Belgesi (2).txt","r")  
f.close()
f=open("Yeni Metin Belgesi (2).txt","w") #dosyanın içerigini siler
f.close()
f=open("Yeni Metin Belgesi (2).txt","a")
f.close()
#%%
f=open("dosyaornegi.txt","a") #yeni dosya acıp yazı yazmaya yarar 
f.write("Selamün Aleyküm")  
f.close()
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:22:55 2019

@author: Doğan AY
"""
takımlar=["Galatasaray","Fenerbahce","Besiktaş","Sivasspor"]

for takım in takımlar:
       if takım =="Besiktaş":
             break
       print(takım + " takımların bilbord gösterimi=" +takım[0:3])
       print("****")
       
#%% For range     
for x in range (1,10):
    print(x+1+1)
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:52:28 2019

@author: Doğan AY
"""


    
aranan="AHMET"
gorunen="-"*len(aranan)  #kaç harfli olduğunu listelemek için kullanıyoruz 
while aranan!=gorunen:
    harf=input(gorunen+"harf ver=")
    for i in range (0,len(aranan)):
        if harf==aranan[i]:
            gorunen=gorunen[:i]+harf+gorunen[i+1:]
print("Congralatiouns")
#%%
import random
import string
aranan=random(stringLength=4)
letters = string.ascii_lowercase
for i in range(stringLength):
    gorunen="-"*len (aranan)
    while aranan!=gorunen:
        harf=input(gorunen+"harf verebilir misiniz = " )
        for i in range (0,len(randomString)):
            if harf==randomString[i]:
                gorunen=gorunen[:i]+harf+gorunen[i+1:]
print ("Bilgisayarın verdiği kelime ", aranan)
print("Congralatiouns")
#%%
import random
import string
def randomString(stringLength=6):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))
def __init__(self):
    gorunen="-"*len(randomString())
    harf=input(gorunen+"harf ver =")
    for i in range (0,len(randomString())):
        if harf==randomString[i]:
            gorunen==gorunen[:i]+harf+gorunen[i+1:]
print("Bilgisayarın tanımladığı kelime",randomString())
print("Congralatiouns")
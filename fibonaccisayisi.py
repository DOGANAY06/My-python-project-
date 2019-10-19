# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:49:54 2019

@author: Doğan AY
"""

ustdeger=int(input("Üst değeri giriniz="))
altdeger=int(input("Alt değeri giriniz="))
i=1
a=0
b=1
for i in range (altdeger,ustdeger):
    c=a+b
    a=b
    b=c
print("Terimlerin toplamı=",i=i+1)
#%%
ustdeger=int(input("Lütfen üst limiti giriniz="))
toplam=0
a=1
b=int(input("Alt değeri giriniz="))
while b<ustdeger:
    print(a)
    c=a+b
    a=b
    b=c
    toplam=toplam+1
#%%
import random
hak=3
list=["tas","kagıt","makas"]
b=random.choice(list)
for x in range (0,3):
    user=str(input("taş kağıt makas  birini seciniz,oyunu bitirmek için q basınız="))
    if  user=="tas" and b=="tas":
        print("Berabere")
        print("Bilgisayarın seçtidiği",b)
    elif user=="kagıt" and b=="kagıt":
        print("Berabere=")
        print("Bilgisayarın seçtidiği",b)
    elif user=="makas" and b=="makas":
        print("Berabere")
        print("Bilgisayarın seçtidiği",b)
    elif user=="kagıt" and b=="makas":
        print("Makas kağıdı keser,kaybettiniz")
        print("Bilgisayarın seçtidiği",b)
    elif user=="makas" and b=="kagıt":
        print("Makas kağıdı keser,kazandınız")
        print("Bilgisayarın seçtidiği",b)
        hak=hak-1
        if hak>=2:
            print("Oyunu siz kazandınız tebrik ederiz=")
    elif user=="tas" and b=="makas":
        print("Taş makası kırar,kazandınız=")
        print("Bilgisayarın seçtidiği",b)
        hak=hak-1
        if hak>=2:
            print("Oyunu siz kazandınız tebrik ederiz=")
    elif user=="makas" and b=="tas":
        print("Tas makası kırar,kaybettiniz=")
        print("Bilgisayarın seçtidiği",b)
    elif user=="kagıt" and b=="tas":
        print("Kağıt taş sarar  kazandınız=")
        print("Bilgisayarın seçtidiği",b)
        hak=hak-1
        if hak>=2:
            print("Oyunu siz kazandınız tebrik ederiz=")
    elif user=="tas" and b=="kagıt":
        print("Kağıt tası sarar kaybettiniz=")
        print("Bilgisayarın seçtidiği",b)
    elif user=="q" or user=="Q":
        break
    else:
        print("Yanlış tuşlama yaptınız")
        print("Bilgisayarın seçtidiği",b)
main()
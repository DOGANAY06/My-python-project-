# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:09:28 2019

@author: Doğan AY
"""

ad=input("Adını Giriniz=")

print("İlk Karakter",ad[0])

print("İkinci Karakter",ad[1])

print("Son karakter",ad[-1])

print("İlk üç karakter",ad[0:3])

print("İlk üç karakter",ad[:3])

print("Anne kızlık soyadı son 2 karakter=",ad[-1])
print("Anne kızlık soyadı son 2 karakter=",ad[-2])
#%%
annesoyadı="TURGUT"
parca=annesoyadı[0:2]
cevap=input("Lütfen Anne kızlık soy isminizin 1. ve 2. karekterinizi yazınız=")
if cevap.upper()==parca:
    print("Cevabınız doğrudur")
elif cevap.lower()==parca:
    print("Cevabınız doğrudur")
else:
    print("Cevap yanlıştır")
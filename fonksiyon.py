# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:37:43 2019

@author: Doğan AY
"""
def kare_al(x):
    return x**2
a=kare_al(7)
print(a)
help(print)
a=[1,2,3,4]
print(len(a))
print(abs(-5))
print(max(a))
print(min(a))
print(sum(a))
#%%
sayi1=int(input("Sayıyı giriniz="))
sayi2=int(input("Sayıyı giriniz="))
def carpim(sayi1,sayi2):
    return sayi1*sayi2
carpim(sayi1,sayi2)
print(carpim)
#%%
def karesi(x):
    return (x**2,x**3)
print(karesi(2))
#%%
def power(n):
    n=int(input("Karesini almak istediğiniz sayıyı giriniz="))
    def calculate_x(x):
        x=int(input("Sayıyı giriniz="))
        return x**n
    return calculate_x
print(karesi)
#%%
x=int(input("Sayıyı giriniz="))
n=int(input("Ne alınacağını giriniz="))
    def hesaplama():
        return x**n
hesaplama()
print(hesaplama)
#%%
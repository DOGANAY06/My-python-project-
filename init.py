# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:22:19 2019

@author: Doğan AY
"""
sayi1=int(input("1.Sayıyı giriniz="))
sayi2=int(input("2.Sayıyı giriniz="))
class Islem4:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
    def topla(self):
        return self.sayi1+self.sayi2
    def cikar(self):
        return self.sayi1-self.sayi2
    def carp(self):
        return self.sayi1*self.sayi2
    def bol (self):
        return self.sayi1/self.sayi2
islem4=Islem4(sayi1,sayi2)
print("Carpma="+str(islem4.carp()))
#%%
Firstname=str(input("First name enter="))
lastName=str(input("Last name enter="))
age=int(input("How old are you="))
class Person:
     def __init__(self,Firstname,lastName,age):
         self.Firstname=Firstname
         self.lastName=lastName
         self.age=age
         
person1=Person(Firstname,lastName,age)
print(person1.Firstname)
print(person1.lastName)
print(person1.age)

class Worker (Person):
    def __init__(self,salary):
        self.salary=salary
class Customer (Person):
    def __init__(self,loan):
        self.loan=loan
ahmet=Worker()

mehmet=Customer()

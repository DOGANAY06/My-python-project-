# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:28:17 2019

@author: Doğan AY
"""

class Person:
    def __init__(self,isim:str,soyisim:str,tcno:int):
        self.isim=isim
        self.soyisim=soyisim
        self.tcno=tcno
class Calismayan(Person):
    pass
class Calisan(Person):
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,salary:int):
        Person.__init__(self,isim,soyisim,tcno)
        self.idno=idno
class Muhendis(Calisan):
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,salary:int,department:str,computerlanguage:tuple,language=tuple,):
        Calisan.__init__(self,isim,soyisim,tcno,idno,salary)
        self.computerlanguage=computerlanguage
        self.department=department
        self.language=language
class Muhasabeci(Calisan):
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,salary:int,application:tuple):
        Calisan.__init__(self,isim,soyisim,tcno,idno,salary)
        self.application=application
x=Muhendis("Doğan","Ay",115225,5862,3500,"Yazilim Mühendisliği",("Python","C#","C# form","C++"),("İngilizce"),("Anaconda Navigator"))
y=Muhasebeci("Özkan","Bulut",14521,252,3000,("Ms Office","Access"))
print(y.application)
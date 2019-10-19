# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:45:50 2019

@author: Doğan AY
"""

def main():
    startup_message()
    input('Adım 1 i görmek için Enter tuşuna basın.')
    step1()
    input('Adım 2 yi görmek için Enter tuşuna basın.')
    step2()
    input('Adım 3 ü görmek için Enter tuşuna basın.')
    adim3()
    input('Adım 4 ü görmek için Enter tuşuna basın.')
    step4()
    print("program bitti")
def startup_message():
    print('Bu program size nasıl yapılacağını anlatıyor ')
    print('ACME çamaşır kurutma makinesini sökünüz.')
    print('işlemde 4 adım var')
    print()
    step4()
def step1():
    print('Step 1: Kurutucuyu çıkarın ve')
    print('onu duvardan uzaklaştır.')
    print()
def step2():
    print('Step 2: Altı vidayı kurutucunun arkasındançıkarın')
    print()
def adim3():
    print('Step 3: Arka paneli kurutucudan çıkarın.')
    print()
def step4():
    print('Step 4: Kurutma makinesinin üst kısmını doğrudan yukarı çekin..')
main()



# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:56:55 2019

@author: Doğan AY
"""
f=open("ornekdosya.txt")
print(f.read())
f.close()
#%%
f=open("ornekdosya.txt")
print(f.readline())
print("<<<<ilk satırda yazan")
print(f.readline())
print("<<<<<<ikinci satırda yazan")
f.close()
#%%
f=open("ornekdosya.txt")
for i,satir in enumerate(f):
    print("{}.Satır".format(i))
    print(satir)
f.close()
#%%
f=open("ornekdosya.txt")
f.write("\n Hi I am Dogan")
f.close()

#%% kolay yollu kapatma
with open("ornekdosya.txt")as f :
    print(f.read())
#%%
    class ornek_cm():
        def __init__(self,dosyadi,mod):
            print("init metodu çağırıldı")
            self.dosyadi=dosyadi
            self.mod=mod
            self.dosya=None
        def __enter__(self):
            print("\n Enter metodu çağrıldı")
            print("Dosya adı {}".format(self.dosyadi))
            self.dosya=open(self.dosyadi,self.mod)
            return self.dosya
        def __exit__(self,exc_type,exc_value,exc_traceback):
            print("\n Exit metodu çağırıldı")
            print("Dosya kapanacak birazdan!")
            self.dosya.close()
#%%
with ornek_cm("test.txt","w" ) as f:
    f.write("Test")
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:20:48 2019

@author: Doğan AY
"""

import os 
if os.name=="nt":
    print("Windows kullanıyorsunuz")
else:
    print("Windows değil")
#%%
import turtle
turtle.home()
turtle.fd(100)
#%%
from datetime import datetime  # modül cağırma işlemi
simdi=datetime.now()
print(simdi.year)
print(simdi.hour)
print(simdi.month)
print(simdi.timetuple)
print(simdi.isocalendar)
#%%
import calendar 
takvim=calendar.TextCalendar(calendar.THURSDAY) #takvim modülü takvim yapar 
takvim.prmonth(2019,8)  #hangi ayın takvimini yapılmasını istediğimizi yazdık 
takvim.pryear(2019)  #bütün senenin takvimini çıkardı 
#%%
import subprocess #arama modülü sp kısaltmasıyla çalışabilir 
program=input("Hangi programı çalıştırmak istiyorsunuz exe yi yazmayı unutmayın=")
subprocess.call(program)
#%%
import subprocess as sp 
iplistesi=["193.255.128.7","127.0.0.1"]
for ip in iplistesi:
    p=sp.Popen("ping"+ip,stdout=sp.PIPE)
    p.wait()
    if p.poll():
        print(ip+"Çalışmayan ip")
    else:
        print(ip+"Çalışan ip")
#%%
import webbrowser as wb 
wb.open("www.youtube.com")
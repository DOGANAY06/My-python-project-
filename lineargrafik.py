# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:23:05 2019

@author: Doğan AY
"""

import matplotlib.pyplot as plt 
fig_size=[16,9]
import numpy as np #her derde deva bir kütüphane
x=np.linspace(0,np.pi*2,500)
# y eksenindeki veriyi de oluşturalım 
y=np.sin(x)
plt.figure() #figurün oluşmasını sağlar
plt.plot(x,y) #figürü gorsel yapar
plt.show() #figüru görsel yapar  ekrana yazdırır 
plt.figure()
plt.plot(x,y)
plt.ylabel("y değişkeni")
plt.xlabel("x değişkeni")
plt.title("Sinüs grafigi")
plt.grid()

plt.figure(figsize=fig_size)
plt.plot(x,y,"-ob") #- cizginin cinsi  o noktoları belirgin yapar
plt.plot(x,y*0.3,"--r",linewidth=4)
plt.ylabel("y ekseni")
plt.xlabel("x ekseni")
plt.title("Ornek cizgi grafiği")
plt.grid()
plt.legend(["Normal sinus","Kesisen cizgi "])
plt.xticks([0,np.pi/2,np.pi,1.5*np.pi,2*np.pi],["0","1","2","3","4"]
plt.annotate("Tam bu noktayı işaretle!..\n (0)",[np.pi,0],[1.5*np.pi,0.6]
             arrowprops=dict(facecolors='m',shrink=0.05),fontsize=15,colors='g')  
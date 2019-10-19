#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt 
labels=["Türkiye","Hindistan","Amerika","Cin","Vietnam"]
sizes=[1,2,3,4,0]
explode=(0.01,0,0,0,0) # çıkıntılı yapar istenilen veriyi pie eklemeyi unutma 
plt.figure()
plt.pie(sizes , labels=labels,autopct="%1.2f%%",explode=explode,
       shadow=True,startangle=90)
plt.title("Yazılım Gelişimi ülkelere göre")


# In[52]:


import numpy as np 
import matplotlib.pyplot as plt 
x=np.random.rand(3)
y=np.random.rand(7)
z=np.sqrt(x**2 + y**2)
plt.figure()
plt.subplot(233)
plt.scatter(x,y, s=90, c=z,marker=">")
plt.subplot(235)
plt.scatter(x,y, s=40, c=z,marker="<")


# In[88]:


import numpy as np 
import matplotlib.pyplot as plt 
x=np.random.rand(7)
y=np.random.rand(7)
z=np.sqrt(x**2 + y**2)
plt.figure()
plt.subplot(122)
plt.scatter(x,y, s=80, c=z,marker=">")
plt.subplot(121)
plt.scatter(x,y, s=90 , c=z,marker="<")


# In[101]:



fig1=plt.figure()
print(".....Figür sınıfı")
print(type(fig1))
ax1=fig1.add_axes([0.2,0.5,0.4,0.8])
print(".....Eksen Sınıfı")
print(type(ax1))


# In[105]:


x=np.linspace(0,5,15)
y=2*x+1
l1=ax1.plot(x,y)
print("\n Dikkat plot çıktısı liste olarak görünecektir bu sizi şaşırtmasın :)")
print(type(l1))
print("Line nesnesinin kendisi burada ")
print(type(l1[0]))


# In[139]:


get_ipython().run_line_magic('matplotlib', 'inline')
fig2=plt.figure()
ax1=fig2.add_axes([0.1,0.2,0.5,0.8,0.09])
ax2=fig2.add_axes([0.2,0.1,0.4,0.7,0.19])
x=np.linspace(1,5,20)
y=2*x+1
fig2=ax1.plot(x,y)
fig2=ax2.plot(x,y,"b")
ax1.spines["bottom"].set_color("red")
ax1.spines["top"].set_color("pink")
ax1.spines["right"].set_color("yellow")
ax1.spines["left"].set_color("brown")

ax2.spines["bottom"].set_color("orange")
ax2.spines["top"].set_color("purple")
ax2.spines["righ"].set_color("black")
ax2.spines["left"].set_color("blue")
ax1.set_title("Büyük eksen")
ax2.set_title("Kücük eksen")
plt.show()


# In[ ]:





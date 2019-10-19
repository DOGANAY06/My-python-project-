#!/usr/bin/env python
# coding: utf-8

# In[1]:


liste=["doğan","hatice"]
print(liste)


# In[2]:


dir(liste)


# In[5]:


for i in dir(liste):
    if i[0]!="_":
        print(i)


# In[6]:


def f():
    print("Hello World")


# In[7]:


f()


# In[8]:


def f(x,y):
    toplam=x+y
    print("Toplam",toplam)
x=int(input("Sayıyı giriniz="))
y=int(input("Sayıyı giriniz="))
f(x,y)


# In[ ]:


def f(*args):
    return args[0]
f=int(input("Sayı giriniz="))


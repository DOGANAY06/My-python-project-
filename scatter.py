#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt 
fig_size = [16,9]
import numpy as np
colors=["r","b","g"]
shapes=[r"$\alpha$",r"$\beta$",r"$\gamma$"]
plt.figure(figsize=fig_size)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
for i,name in enumarete[iris.target_names]:
    plt.scatter(iris.data[iris.target==i,0],iris.data[iris.target==i,1],s=iris.data[iris.target==i,2]*70,c=colors[i],marker=shapes[i],alpha=0,3)
    lgnd=plt.legend(iris.targe_names)   
    lgnd=legendHandles[0]._sizes=[70]
    lgnd=legendHandles[1]._sizes=[70]
    lgnd=legendHandles[2]._sizes=[70]


# In[ ]:





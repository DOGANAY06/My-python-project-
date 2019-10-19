# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:05:47 2019

@author: Doğan AY
"""

import numpy as np 
a=np.floor(49*np.random.random((2,6)))
print(a)
print(a.shape)
print(a.ravel())
print(a.shape)
print(a.reshape(2,6))
a=a.reshape(1,12)
print(a.T)
print(a.reshape(2,-1))
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:34:23 2019

@author: Doğan AY
"""

sayilar=[21,23,24,25,26,27,28]
sayilarinkaresi=list(map(lambda x:x*x,sayilar))
print(sayilarinkaresi)
sayilarifilter=list(filter(lambda x: x>500,sayilarinkaresi))
print(sayilarifilter)
from functools import reduce 
sayilarfaktoriyel=reduce(lambda x,y:x*y,sayilar)
print(sayilarfaktoriyel)
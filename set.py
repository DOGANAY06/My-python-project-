# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 00:44:25 2019

@author: Doğan AY
"""

kume={1,2,3,4,5,"elma","armut"}
print("elma" in kume )
kume.add(42)
kume.update([15,"ayva"])
print(len(kume))
kume.remove("ayva")
kume.discard("ayva")

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 01:03:58 2019

@author: Doğan AY
"""

import json 
data='{"firstName":"Dogan","lastname":"ay"}'

y=json.loads(data)
print(y["firstName"])

customer={
        "firstName":"Dogan",
        "email":"doganay@hotmail.com"
        }
customerJson=json.dumps(customer)
print(customer)
print(json.dumps("Ahmet"))
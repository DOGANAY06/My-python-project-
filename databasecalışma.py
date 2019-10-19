# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:16:28 2019

@author: Doğan AY
"""

import sqlite3 
connection=sqlite3.connect("chinook.db")
cursor =connection.execute("select * from customers")
for row in cursor:
    print("First Name="+row[1])
    print("Last Name="+row[2])
    print("******")

connection.close()

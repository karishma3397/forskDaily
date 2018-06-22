# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:36:27 2018

@author: KC
"""

import re
regex = re.compile(r'^[+-]?[0-9]*\.[0-9]+')
#match() used for beginning
#search() gives first found
#findAll() returns all in form of list
#finditer() returns all found in form of object 
list1 = []
while True:
    str1 = input()
    if not str1:
        break
    list1.append(str1)
for i in list1:
    response = regex.match(i)
    if response:
        print("True")
    else:
        print("False")

# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:53:09 2018

@author: KC
"""
from collections import OrderedDict
od = OrderedDict()

while True:
    str1 = input()
    if not str1:
        break
    list1 = str1.split(' ')
    value = list1[-1]
    key = ' '.join(list1[0:-1])
    if key in od:
        od[key] = od[key]+int(value)
    else:
        od[key] = int(value)
        
for k,v in od.items():
    print(k,v)

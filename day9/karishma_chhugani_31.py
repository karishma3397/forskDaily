# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:09:16 2018

@author: KC
"""
import re
regex = re.compile(r'^[a-z0-9-_]+@[a-z0-9]+\.[a-z]{2,4}$')
list1 = []
while True:
    N = input()
    if not N:
        break
    list1.append(N)
list2=[]
for i in list1:
    response = regex.match(i)
    if response:
        list2.append(i)
        
list2.sort()
print(list2)

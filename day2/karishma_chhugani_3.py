# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:35:00 2018

@author: KC
"""

text = input("enter string")
lst=[]
print(len(text))
for i in text:
    if i == (text[len(text)-1]):
        lst.append(i)
    else:
        
        lst.append(i+"*")
        

str1 = ''.join(lst)
print(str1)
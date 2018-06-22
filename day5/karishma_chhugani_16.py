# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:33:58 2018

@author: KC
"""

lst = []
def translate(text):
    
    for i in text:
        if i in ['a','e','i','o','u']:
            lst.append(i)
        elif i==" ":
            lst.append(i)
        else:
            lst.append(i+"o"+i)
    return lst
text = input("enter string")
translate(text)

str1 = ''.join(lst)
print(str1)
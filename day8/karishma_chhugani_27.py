# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:31:28 2018

@author: KC
"""



str1 = str(input("ENTER"))
l1 = str1.split(' ')
def palindrome():
    for i in l1:
        if i =="".join( reversed(i)):
            return(True)
    return(False)
print(palindrome())
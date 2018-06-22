# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:54:40 2018

@author: KC
"""
text  = input("enter string") # input from user
import string

def Panagram(text):
    text = text.lower() #converting user input to lowe case
    alphacount = dict( (key, 0) for key in string.ascii_lowercase) # making a dictionary and setting value of each alphabet to 0
    for i in text:
        alphacount[i] = 1 # if alphabet is found: set the value of that alphabet to 1
    for alpha , count in alphacount.items():
        if count == 0: #if any alphabet count is zero, the string is not panagram
            return('not panagram')
    return('panagram')
print(Panagram(text))
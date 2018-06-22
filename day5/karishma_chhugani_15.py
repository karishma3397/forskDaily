# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:26:25 2018

@author: KC
"""
def fizzbuzz(n):
    if n%15 == 0:
        print ("fizzbuzz")
    elif n%3==0:
        print("fizz")
    elif n%5 == 0:
        print("buzz")
    else :
        print(n)
        
for n in range(1,51):
    fizzbuzz(n)
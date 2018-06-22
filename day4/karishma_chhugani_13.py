# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:08:19 2018

@author: KC
"""

def pyramid(n):
    
    for i in range(1,n+1):
       print (i*"*")
    for i in range(n,0,-1):
        print (i*"*")
print("enter n")
n=input()
pyramid(int(n))
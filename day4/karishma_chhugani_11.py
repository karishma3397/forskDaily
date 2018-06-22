# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:31:11 2018

@author: KC
"""

#submission 11
list = [5,2,6,2,3]
import functools

def Add(x,y) : return x+y
print('Add =',functools.reduce(Add,list))

def Multiply(x,y): return x*y
print('Multiply =',functools.reduce(Multiply,list))

def Largest(x,y): return max(x,y)
print('Largest =',functools.reduce(Largest,list))

def Smallest(x,y): return min(x,y)
print('Smallest =',functools.reduce(Smallest,list))

def Sorting(list): return sorted(list)
print('Sorted =', Sorting(list))

def Remove_Duplicates(list) : return (set(list))
print ('Without Duplicates =',Remove_Duplicates(list))
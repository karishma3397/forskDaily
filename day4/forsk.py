# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:30:33 2018

@author: KC
"""
# func_doc : used to print the function string 
# in-built functions: filter, map and reduce

def f(x) : return x%3 == 0 or x%5==0
     
list(filter(f, range(2,25)))
#returns the list of values which are true

def cube(x): return x*x*x
        
list(map(cube, range(1,11)))
list(map(lambda x : x*x*x , range(1,11)))

import functools
def add(x,y) : return x+y
functools.reduce(add,range(1,11))

#%%
words =['It', 'is', 'raining' , 'cats' , 'and' , 'dogs']
list(map(lambda words: len(words), words))
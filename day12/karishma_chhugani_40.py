# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:07:42 2018

@author: KC
"""
import numpy as np
num = input ("enter integers")
k = list(num.split(' '))
results = list(map(int, k))
a = np.asarray(results)
b = a.reshape(3,3) 
print (b) 

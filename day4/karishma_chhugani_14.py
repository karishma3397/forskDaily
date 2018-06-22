# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:31:17 2018

@author: KC
"""

def fix_teen(value):
    lst =[13,14,17,18,19]
    if value in lst:
        return 0
    else:
        return value
        
        
dictionary = input("enter dictionary")

import ast

act_dictionary = ast.literal_eval(dictionary)
sum1=0
for i in act_dictionary.values():
    
    value_teen = fix_teen(i)
    sum1 = sum1 + value_teen
    
print(sum1)
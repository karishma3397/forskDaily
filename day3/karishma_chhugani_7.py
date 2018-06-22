# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:18:06 2018

@author: KC
"""
import collections
text = input("enter string")
d=collections.Counter(text).most_common()
for word, count in d:
	print(word, ": ", count)

    
        
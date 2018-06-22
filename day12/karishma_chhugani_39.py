# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:03:14 2018

@author: KC
"""

import numpy as np
randarr = np.random.randint(1,16,10)
l=np.bincount(randarr)
from collections import Counter
Counter(randarr).most_common(1)[0][0]

d={}
for i in randarr:
    if i in d.keys():
        d[i]+=1
    else:
         d[i]=1
k=max(d.values())
l = (list(d.keys())[list(d.values()).index(k)])
print(l)
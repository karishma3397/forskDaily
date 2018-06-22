# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:48:35 2018

@author: KC
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100,20.0,1000)
print(incomes)
plt.hist(incomes,50)
plt.show()
print(np.mean(incomes))
print(np.median(incomes))
incomes = np.append(incomes,1000000)
print(np.mean(incomes))
print(np.median(incomes))

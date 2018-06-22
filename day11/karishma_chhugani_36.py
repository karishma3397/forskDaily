# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:40:10 2018

@author: KC
"""

import pandas as pd
train = pd.read_csv("training_titanic.csv")
train["Child"] = 0
train["Child"][train["Age"]<18] = 1
print("Child survived:",train['Survived'][train['Child']==1].value_counts(normalize=True)[1]*100)
print("Child died:",train['Survived'][train['Child']==1].value_counts(normalize=True)[0]*100)
print("Old survived:",train['Survived'][train['Child']==0].value_counts(normalize=True)[1]*100)
print("Old died:",train['Survived'][train['Child']==0].value_counts(normalize=True)[0]*100)

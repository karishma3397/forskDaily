# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:55:03 2018

@author: KC
"""

import pandas as pd
train = pd.read_csv("training_titanic.csv")
print(train["Survived"].value_counts())
print(train["Survived"].value_counts(normalize = True))
print("Male survived:",train['Survived'][train['Sex']=='male'].value_counts(normalize=True)[1]*100)
print("Male died:",train['Survived'][train['Sex']=='male'].value_counts(normalize=True)[0]*100)
print("Female survived:",train['Survived'][train['Sex']=='female'].value_counts(normalize=True)[1]*100)
print("Female died:",train['Survived'][train['Sex']=='female'].value_counts(normalize=True)[0]*100)
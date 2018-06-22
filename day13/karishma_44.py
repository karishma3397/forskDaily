# -*- coding: utf-8 -*-
"""
Created on Thu May 31 08:50:48 2018

@author: KARIS
"""

import pandas as pd
df = pd.read_csv("Cars.csv")

for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])
    
features = df.iloc[: ,1:12]
labels = df.iloc[:,0]

from sklearn.model_selection import train_test_split
features_train , features_test, labels_train , labels_test = train_test_split(features , labels , test_size = 0.5 , random_state = 0)
print(features_train)
print(features_test)
print(labels_train)
print(labels_test)
features_train.to_csv("features_train.csv")
features_test.to_csv("features_test.csv")
labels_train.to_csv("labels_train.csv")
labels_test.to_csv("labels_test.csv")
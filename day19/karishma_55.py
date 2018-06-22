# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:54:00 2018

@author: KARIS
"""

import pandas as pd
df = pd.read_csv("PastHires.csv")
features =  df.iloc[:,:-1].values
labels = df.iloc[:,-1:].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1]=labelencoder.fit_transform(features[:,1])
features[:,3]=labelencoder.fit_transform(features[:,3])
features[:,4]=labelencoder.fit_transform(features[:,4])
features[:,5]=labelencoder.fit_transform(features[:,5])

labels[: , -1] = labelencoder.fit_transform(labels[: , -1])


#from decision tree
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features , labels)

import numpy as np
labels_pred = regressor.predict(np.array([10,1,4,0,1,0]).reshape(1,-1))
labels_pred_2 = regressor.predict(np.array([10,0,4,1,0,1]).reshape(1,-1))

#from random forest
from sklearn.ensemble import RandomForestRegressor
reg2 = RandomForestRegressor(n_estimators= 10,random_state = 0)
reg2.fit(features, labels)
labels_pred_3 = reg2.predict(np.array([10,1,4,0,1,0]).reshape(1,-1))
labels_pred_4 = reg2.predict(np.array([10,0,4,1,0,1]).reshape(1,-1))

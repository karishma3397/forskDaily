# -*- coding: utf-8 -*-
"""
Created on Thu May 31 09:16:14 2018

@author: KARIS
"""

import pandas as pd

df = pd.read_csv("Foodtruck.csv")

features = df.iloc[:,:1].values
labels = df.iloc[:,-1].values

from sklearn.cross_validation import train_test_split
features_train,features_test , labels_train , labels_test = train_test_split(features , labels , test_size = 0.2 ,random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train , labels_train)

#jaipur population profit
labels_pred = regressor.predict(3.073)

#visualization
import matplotlib.pyplot as plt
plt.scatter(features_train ,  labels_train ,  color = 'red')
plt.plot(features_train,regressor.predict(features_train),color = 'blue')
plt.show()

plt.scatter(features_test , labels_test , color= 'red')
plt.plot(features_train,regressor.predict(features_train),color = 'blue')
plt.show()


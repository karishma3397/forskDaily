# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:26:16 2018

@author: KARIS
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('bluegills.csv')
features = df.iloc[:,0:1].values
labels = df.iloc[: , 1:2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features , labels)
print(lin_reg.predict(5))
plt.scatter(features, labels , color = 'red')
plt.plot(features,lin_reg.predict(features),color = 'blue')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poln_object = PolynomialFeatures(degree = 2)
features_poln = poln_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poln,labels)

print(lin_reg_2.predict(poln_object.fit_transform(5)))

plt.scatter(features, labels,color = 'red')
plt.plot(features , lin_reg_2.predict(poln_object.fit_transform(features)))
plt.show()

features_grid  = np.arange(min(features), max(features) , 0.1)
features_grid = features_grid.reshape((-1,1))
plt.scatter(features,labels , color = 'red')
plt.plot(features_grid , lin_reg_2.predict(poln_object.fit_transform(features_grid)))
plt.show()
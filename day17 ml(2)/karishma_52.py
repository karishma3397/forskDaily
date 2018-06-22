# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:56:06 2018

@author: KARIS
"""

import pandas as pd
import numpy as np

df = pd.read_csv("iq_size.csv")

#splitting features and labels
features = df.iloc[: , 1:].values
labels = df.iloc[: , :1].values


#train test and split
from sklearn.model_selection import train_test_split
features_train, features_test, label_train , label_test = train_test_split(features , labels ,  test_size = 0.2, random_state = 0)


#multilinear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train , label_train)


#prediction by passing an array of brainsize height and weight
pred = regressor.predict(np.array([90 , 70 , 150]).reshape(1,-1))


#optimal model to predict which feature is more important for a given label using backward elimination
import statsmodels.formula.api as sm
features = np.append(arr = np.ones((38,1)).astype(int), values = features , axis =1)
features_opt = features[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[1,2]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[1]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

#Brain is mainly affecting the intelligence
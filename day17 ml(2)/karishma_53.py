# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:41:08 2018

@author: KARIS
"""

import pandas as pd
import numpy as np

df = pd.read_csv("stats_females.csv")

features = df.iloc[: , 1:].values
labels = df.iloc[: , :1].values

from sklearn.model_selection import train_test_split
features_train, features_test, label_train , label_test = train_test_split(features , labels ,  test_size = 0.2, random_state = 0)


#multilinear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train , label_train)

import statsmodels.formula.api as sm
features = np.append(arr = np.ones((214,1)).astype(int), values = features , axis =1)
features_opt = features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

#When Father’s Height Is Held Constant, The Average Student Height Increases 
#By How Many Inches For Each One-Inch Increase In Mother’s Height.
#When Mother’s Height Is Held Constant, The Average Student Height Increases 
#By How Many Inches For Each One-Inch Increase In Father’s Height.
print(regressor_OLS.params[1] , "dad's height constant")
print(regressor_OLS.params[2] , "mom's height constant")
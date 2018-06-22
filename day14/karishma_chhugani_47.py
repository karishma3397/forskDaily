# -*- coding: utf-8 -*-
"""
Created on Wed May 30 00:17:36 2018

@author: KARIS
"""

import pandas as pd
df = pd.read_csv('Loan.csv')
df = df.drop(['Loan_ID'],axis = 1)

for column in ['Gender', 'Married', 'Dependents','Education','Self_Employed']:
    df[column] = df[column].astype('category')
    df[column]= df[column].cat.codes
df = pd.get_dummies(data=df, columns=['Property_Area'])
from sklearn.model_selection import train_test_split
features =  df.iloc[:,:-1].values
labels = df.iloc[:,-1].values
features_train, features_test, label_train , label_test = train_test_split(features , labels ,  test_size = 0.2, random_state = 0)

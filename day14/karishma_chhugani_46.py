# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:17:27 2018

@author: KARIS
"""


import pandas as pd
data = pd.read_csv("Loan.csv")

data = data.drop(['Loan_ID'],axis = 1)
features =  data.iloc[:,:-1].values
labels = data.iloc[:,-1:].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
labelencoder = LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
features[:,1]=labelencoder.fit_transform(features[:,1])
features[:,2]=labelencoder.fit_transform(features[:,2])
features[:,3]=labelencoder.fit_transform(features[:,3])
features[:,4]=labelencoder.fit_transform(features[:,4])
features[:,10]=labelencoder.fit_transform(features[:,10])
onehotencoder = OneHotEncoder(categorical_features = [-1])
features = onehotencoder.fit_transform(features).toarray()

features_train, features_test, label_train , label_test = train_test_split(features , labels ,  test_size = 0.2, random_state = 0)
labels= labelencoder.fit_transform(labels)
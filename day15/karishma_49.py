# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:48:09 2018

@author: KARIS
"""

import pandas as pd
df = pd.read_csv("Red_Wine.csv")

#handling missing values
#df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
# or 
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])
    
#splitting features and labels
features =  df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

#applying one hot encoding on catagorical data
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
labelencoder = LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

#train_test_split
from sklearn.model_selection import train_test_split
features_train , features_test ,labels_train , labels_test = train_test_split(features , labels ,  test_size = 0.2, random_state = 0)  

#scailing
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)
    



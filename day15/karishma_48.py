# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:20:26 2018

@author: KARIS
"""

import pandas as pd
url = 'https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv'
df = pd.read_csv(url , 
                 header = None, 
                 usecols = [0,1,2] , 
                 sep= ',', 
                 names = ['Class label', 'Alcohol', 'Malic acid'] )

features =  df.iloc[:,1:3].values
labels = df.iloc[:,0].values

from sklearn.model_selection import train_test_split
features_train, features_test, label_train , label_test = train_test_split(features , labels ,  test_size = 0.2, random_state = 0)

#either min max scailing or standard scailing
#from sklearn.preprocessing import MinMaxScaler
#scaler = MinMaxScaler()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)


# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:57:09 2018

@author: KARIS
"""
#importing libraries
import pandas as pd


#importing dataset
df = pd.read_csv("mushrooms.csv")

#checking for null values
df.isnull().any()

df_new = df.iloc[: , [0,5,21,22]]
features = df_new.iloc [: , 1: ].values
labels = df_new.iloc[: , 0:1].values

from sklearn.preprocessing import LabelEncoder ,OneHotEncoder

le = LabelEncoder()
ohe = OneHotEncoder(categorical_features = [0,1,2])

features[:,0]=le.fit_transform(features[:,0])
features[:,1]=le.fit_transform(features[:,1])
features[:,2]=le.fit_transform(features[:,2])


labels = le.fit_transform(labels)


features = ohe.fit_transform(features).toarray()


from sklearn.model_selection import train_test_split as TTS
features_train , features_test,labels_train , labels_test = TTS(features ,labels , test_size = 0.3 , random_state = 0)


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors = 5 , p = 2)
clf.fit(features_train , labels_train)

pred = clf.predict(features_test)

Score = clf.score(features_test , labels_test)

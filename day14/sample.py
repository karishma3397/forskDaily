# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:44:29 2018

@author: KARIS
"""

import pandas as pd
df = pd.read_csv("Cricket_Salary_Data.csv")
features=df.iloc[: , : -1].values
labels= df.iloc[: , -1:].values

from sklearn.preprocessing import Imputer as ip
imp = ip(missing_values = 'NaN' , strategy = "median" , axis=0)
imp = imp.fit(features[: ,1:2 ])

features[: , 1:2] = imp.transform(features[: , 1:2])


from sklearn.preprocessing import LabelEncoder
le =LabelEncoder()
le = le.fit(features[:,0])
features[:, 0] = le.transform(features[:,0])

from sklearn.preprocessing import OneHotEncoder as OHE
ohe = OHE(categorical_features =[0] )
features = ohe.fit_transform(features).toarray()

labels = le.fit_transform(labels)

from sklearn.model_selection import train_test_split as TTS
x_train ,x_test , y_train , y_test = TTS(features , labels , test_size = 0.4 , random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test) 
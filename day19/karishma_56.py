# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:16:55 2018

@author: KARIS
"""
#importing data
import pandas as pd

df = pd.read_csv("Auto_mpg.txt", delim_whitespace = True ,header = None )

#naming columns
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name']


#finding car whose mpg value is maximum
car = df.iloc[df['mpg'].argmax(),-1]
print("car with maximum mpg is" , car)



#replacing missing values from horsepower column whic are in form of '?'
df['horsepower'][df['horsepower']=='?'] = df['horsepower'].mode()[0]
df['horsepower'] = df['horsepower'].convert_objects(convert_numeric=True)



features = df.iloc[: , 1:-1].values
labels = df.iloc[:,0:1].values




#train test and split
from sklearn.model_selection import train_test_split as TTS
features_train , features_test , labels_train , labels_test = TTS(features , labels , test_size = 0.2 , random_state = 0)




#scailing using standard scaler
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)




#also scailing the required result
import numpy as np
pred_1 = sc.transform(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))





#using decision tree
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features_train , labels_train)
labels_pred = regressor.predict(features_test)
mpg_pred = regressor.predict(pred_1)
Score = regressor.score(features_test, labels_test)
print("mpg value using decision tree is" , mpg_pred , "and the score of model is" , Score*100)



#using random forest 
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators = 100 , random_state = 0 )
reg.fit(features_train , labels_train)

labels_pred_2 = reg.predict(features_test)
mpg_pred_2 = reg.predict(pred_1)
Score2 = reg.score(features_test, labels_test)

print("mpg value using random forest is" , mpg_pred_2 , "and the score of model is" , Score2*100)

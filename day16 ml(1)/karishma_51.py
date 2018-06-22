# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:57:31 2018

@author: KARIS
"""
#import data
import pandas as pd
df = pd.read_csv('Bahubali2_vs_Dangal.csv')


#splitting dependent and independent values
features= df.iloc[:,:1].values
lab_bahu = df.iloc[: ,1:2].values
lab_dang = df.iloc[:,2:3].values


#splitting test and train
from sklearn.model_selection import train_test_split as tts
features_train, features_test, lab_bahu_train, lab_bahu_test,lab_dang_train , lab_dang_test = tts(
        features , lab_bahu, lab_dang , test_size = 0.2 ,random_state = 0)

#fitting data on bahubali's train
from sklearn.linear_model import LinearRegression
reg_bahu = LinearRegression()
reg_bahu.fit(features_train,lab_bahu_train)


#fitting data on dangal's train
reg_dang = LinearRegression()
reg_dang.fit(features_train,lab_dang_train)

#predicting income on 10th day
lab_pred_bahu= reg_bahu.predict(10)
lab_pred_dang= reg_dang.predict(10)


#maximum profit out of bahubali and dangal
l= max(lab_pred_bahu , lab_pred_dang)
if l ==lab_pred_bahu:
    print("bahubali2")
else:
    print("dangal")


#plotting linear regression of bahubali on training data
import matplotlib.pyplot as plt
plt.scatter(features_train, lab_bahu_train,color = 'red')
plt.plot(features_train, reg_bahu.predict(features_train), color = 'blue')
plt.show()


#plotting linear regression of dangal on training data
plt.scatter(features_train, lab_dang_train , color = 'red')
plt.plot(features_train , reg_dang.predict(features_train), color = 'pink')
plt.show()


#plotting line graph of both and scatter points of 10th day
plt.plot(features, lab_bahu , color='red')
plt.plot(features, lab_dang ,color = 'green')
plt.scatter(10 , lab_pred_bahu, color = 'red')
plt.scatter(10,lab_pred_dang ,  color = 'green')
plt.show()

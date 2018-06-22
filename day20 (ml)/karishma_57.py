# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:03:17 2018

@author: KARIS
"""
#importing the libraries
import numpy as np

import pandas as pd




#importing the dataset
df = pd.read_csv('affairs.csv')

features = df.iloc[:,0:-1].values
labels = df.iloc[: , -1:].values





#there are no missing values in the dataset as:
#df.isnull().values.any() is false

#one hot encoding occupation and occupation of husband
#occ : 6 and occ_husb : 7th column

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1,-2])
features = onehotencoder.fit_transform(features).toarray()



#dummy trap handling
features = np.delete(features , [0,6] , axis = 1)



#splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split as TTS
features_train , features_test,labels_train , labels_test = TTS(features ,labels , test_size = 0.3 , random_state = 0)





#fitting logistic regression to the training set
from sklearn.linear_model import LogisticRegression as lg
classifier = lg(random_state = 0)
classifier.fit(features_train , labels_train)




#predicting the test set result
labels_pred = classifier.predict(features_test)




#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix as CM
cm = CM(labels_test , labels_pred)


affair = df["affair"].value_counts(normalize = True)*100


#score of above model
Score = classifier.score(features_test,labels_test)

print("accuracy of model is " ,Score*100 , "%")

#Predict the probability of an affair for a random woman not
# present in the dataset. She's a 25-year-old teacher who 
#graduated college, has been married for 3 years, has 1 child,
# rates herself as strongly religious, rates her marriage 
#as fair, and her husband is a farmer.

pred_affair = classifier.predict(np.array([0,0,1,0,0,1,0,0,0,0,3,25,3,1,4,16]).reshape(1,-1))

probability = classifier.predict_proba(np.array([0,0,1,0,0,1,0,0,0,0,3,25,3,1,4,16]).reshape(1,-1))
if pred_affair[0] == 0:
    print("no extramarital affair")
else :
    print("atleast one affair")
    
print("probability of affair is" , probability[0][1]*100)



#optimal model 


import statsmodels.formula.api as sm
features = np.append(arr = np.ones((6366,1)).astype(int), values = features , axis =1)
features_opt = features[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,6,7,8,9,10,11,12,13,14,15,16]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,11,12,13,14,15,16]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:,[0,11,12,13,15,16]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:,[0,11,12,13,15]]
regressor_OLS = sm.OLS(endog = labels , exog = features_opt).fit()
regressor_OLS.summary()

#depends on rate_marriage , age ,yrs_married and religion
#children , education , occupation and husband's occupation are important 
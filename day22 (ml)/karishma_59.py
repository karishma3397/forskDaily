# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:35:01 2018

@author: KARIS
"""
#importing dataset
import pandas as pd
df = pd.read_csv("tree_addhealth.csv")


#filling missing values
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])
    
'''
The attributes are:
 

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale
'''
#features and labels acc to que1
features = df.iloc[:,:16]
labels = df.iloc[:,7:8]


features.drop(["TREG1"],axis=1, inplace=True)



from sklearn.model_selection import train_test_split as TTS
features_train , features_test, labels_train , labels_test = TTS(features , labels , test_size = 0.2 , random_state = 0)


from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy' , random_state = 0)
classifier.fit(features_train , labels_train)

labels_pred = classifier.predict(features_test)

Score = classifier.score(features_test , labels_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test , labels_pred)

#%%
#que2
df_new = df[["BIO_SEX","VIOL1" , "EXPEL1"]]


feat_new = df_new.iloc[: , 0:2].values
labels_new = df_new.iloc[: , 2:].values



from sklearn.model_selection import train_test_split as TTS
feat_new_train , feat_new_test, labels_new_train , labels_new_test = TTS(feat_new , labels_new , test_size = 0.2 , random_state = 0)


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion = 'entropy' , random_state = 0)
clf.fit(feat_new_train , labels_new_train)

labels_new_pred = clf.predict(feat_new_test)

Score_new = clf.score(feat_new_test , labels_new_test)

from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(labels_new_test , labels_new_pred)

#%%

#que3
df_new_2 = df.iloc[: , [1,2,3,4,5,7]]

feat_new_2 = df_new_2.iloc[: , 0 :5].values
labels_new_2 = df_new_2.iloc[: , 5: ].values



from sklearn.model_selection import train_test_split as TTS
feat_new_2_train , feat_new_2_test, labels_new_2_train , labels_new_2_test = TTS(feat_new_2, labels_new_2 , test_size = 0.2 , random_state = 0)

from sklearn.ensemble import RandomForestClassifier as RFC
clfrfc = RFC(n_estimators = 10 , criterion  = 'entropy', random_state = 0 )
clfrfc.fit(feat_new_2_train ,labels_new_2_train)

labels_new_2_pred = clfrfc.predict(feat_new_2_test)


Score_new_2 = clfrfc.score(feat_new_2_test , labels_new_2_test)

from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(labels_new_2_test , labels_new_2_pred)
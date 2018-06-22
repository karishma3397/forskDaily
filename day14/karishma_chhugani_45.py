# -*- coding: utf-8 -*-
"""
Created on Wed May 30 01:14:31 2018

@author: KARIS
"""

import pandas as pd
data = pd.read_csv("Automobile.csv")


print('data types' ,data.dtypes)

#new dataframe objectdf
objectdf = data.select_dtypes(include=['object'])

#filling nan values with most frequent values
objectdf[objectdf.isnull().any(axis = 1)]
objectdf["num_doors"].value_counts()
objectdf = objectdf.fillna({"num_doors" : "four"})

for i in objectdf:
    objectdf[i] = objectdf[i].fillna(objectdf[i].mode()[0])

#performing label encoding on body_style
objectdf['body_style'] = objectdf['body_style'].astype('category')
objectdf['body_style']= objectdf['body_style'].cat.codes

#performing one hot encoding on drive_wheels and body style
objectdf = pd.get_dummies(data=objectdf, columns=['drive_wheels','body_style'])

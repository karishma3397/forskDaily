# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:27:03 2018

@author: KARIS
"""

#yihui.name/animation :visualize kfold
import pandas as pd
df = pd.read_csv("banknotes.csv")

X = df.iloc[: , 1:-1].values
y = df.iloc[: , -1:].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting logistic regression to the Training set
from sklearn.linear_model import LogisticRegression as lg
classifier = lg(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())


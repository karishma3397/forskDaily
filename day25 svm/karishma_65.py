# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:17:33 2018

@author: KARIS
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("breast_cancer.csv")
df.drop(["A"] , axis = 1 , inplace = True)
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])


features = df.iloc[: , :-1].values
labels = df.iloc[: , -1].values


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_


from sklearn.model_selection import train_test_split as TTS
features_train ,  features_test , labels_train ,  labels_test = TTS(features , labels , test_size = 0.2 , random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf' , random_state = 0)
classifier.fit(features_train , labels_train)

labels_pred = classifier.predict(features_test)


from sklearn.metrics import confusion_matrix as CM
cm = CM(labels_test, labels_pred)


score = classifier.score(features_test , labels_test)



pred_tumor = classifier.predict(pca.transform((np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1))))
'''
from matplotlib.colors import ListedColormap

features_set, labels_set = features_train , labels_train
X1,X2 = np.meshgrid(np.arange(start = features_set[: , 0].min()-1 , stop = features_set[: , 0].max() + 1 ,step = 0.01),
                    np.arange(start = features_set[: , 1].min()-1 , stop = features_set[: , 0].max() + 1 ,step = 0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75 , cmap = ListedColormap(('red','green')))
plt.xlim(X1.min() , X1.max())
plt.ylim(X2.min() , X2.max())
for i,j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j,0] , features_set[labels_set == j,1],
                c = ListedColormap(('red','green'))(i) , label = j)
plt.show()
'''

# Visualising the Training set results
from matplotlib.colors import ListedColormap
features_set, labels_set = features_train, labels_train
X1, X2 = np.meshgrid(np.arange(start = features_set[:, 0].min() - 1, stop = features_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = features_set[:, 1].min() - 1, stop = features_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
features_set, labels_set = features_test, labels_test
X1, X2 = np.meshgrid(np.arange(start = features_set[:, 0].min() - 1, stop = features_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = features_set[:, 1].min() - 1, stop = features_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
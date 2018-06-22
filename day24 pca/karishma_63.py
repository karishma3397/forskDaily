# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:09:01 2018

@author: KARIS
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crime_data.csv")

features  = df.drop(["State" , "UrbanPop"],axis  = 1 ).values

'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)
'''


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++',random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 3 , init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)


plt.scatter(features[y_kmeans == 0,0], features[y_kmeans == 0,1] , s = 50 , c = 'red')
plt.scatter(features[y_kmeans == 1,0], features[y_kmeans == 1,1] , s = 50 , c = 'blue'  )
plt.scatter(features[y_kmeans == 2,0], features[y_kmeans == 2,1] , s = 50 , c = 'green')
#plt.scatter(features[y_kmeans == 3,0], features[y_kmeans == 3,1] , s = 50 , c = 'pink'  )

plt.scatter(kmeans.cluster_centers_[: , 0], kmeans.cluster_centers_[: , 1],s = 200 , c = 'yellow',label = ' Centroids')


plt.title('cluster of pcs')
plt.xlabel('pc1')
plt.ylabel('pc2')

centers = kmeans.cluster_centers_


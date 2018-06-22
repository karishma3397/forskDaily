# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:00:01 2018

@author: KARIS
"""

from sklearn.datasets import load_iris
iris = load_iris()
iris = iris.data


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iris = pca.fit_transform(iris)
explained_variance = pca.explained_variance_ratio_


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++',random_state = 0)
    kmeans.fit(iris)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 3 , init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(iris)


plt.scatter(iris[y_kmeans == 0,0], iris[y_kmeans == 0,1] , s = 50 , c = 'red')
plt.scatter(iris[y_kmeans == 1,0], iris[y_kmeans == 1,1] , s = 50 , c = 'blue'  )
plt.scatter(iris[y_kmeans == 2,0], iris[y_kmeans == 2,1] , s = 50 , c = 'green')
#plt.scatter(features[y_kmeans == 3,0], features[y_kmeans == 3,1] , s = 50 , c = 'pink'  )

plt.scatter(kmeans.cluster_centers_[: , 0], kmeans.cluster_centers_[: , 1],s = 200 , c = 'yellow',label = ' Centroids')


plt.title('cluster of pcs')
plt.xlabel('pc1')
plt.ylabel('pc2')

centers = kmeans.cluster_centers_


# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:24:14 2018

@author: KARIS
"""
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("tshirts.csv")

features  = df.drop(["name"],axis  = 1 ).values

#using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i , init = 'k-means++',random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.Title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()




#fitting kmeans to the dataset
kmeans = KMeans(n_clusters = 3 , init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)


plt.scatter(features[y_kmeans == 0,0], features[y_kmeans == 0,1] , s = 50 , c = 'red' , label = 'small')
plt.scatter(features[y_kmeans == 1,0], features[y_kmeans == 1,1] , s = 50 , c = 'blue' , label = 'medium' )
plt.scatter(features[y_kmeans == 2,0],features[y_kmeans == 2 , 1] , s = 50, c = 'green')
plt.scatter(kmeans.cluster_centers_[: , 0], kmeans.cluster_centers_[: , 1],s = 200 , c = 'yellow',label = ' Centroids')


plt.title('cluster of size of tshirts')
plt.xlabel('height')
plt.ylabel('weight')

centers = kmeans.cluster_centers_
#coordinates of centeroid 
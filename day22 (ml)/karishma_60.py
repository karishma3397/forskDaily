# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:47:24 2018

@author: KARIS
"""
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
df = pd.read_csv("deliveryfleet.csv")
features  = df.drop(["Driver_ID"],axis  = 1 ).values

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
kmeans = KMeans(n_clusters = 2 , init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)


plt.scatter(features[y_kmeans == 0,0], features[y_kmeans == 0,1] , s = 50 , c = 'red' )
plt.scatter(features[y_kmeans == 1,0], features[y_kmeans == 1,1] , s = 50 , c = 'blue')

plt.scatter(kmeans.cluster_centers_[: , 0], kmeans.cluster_centers_[: , 1],s = 200 , c = 'yellow',label = ' Centroids')


plt.title('cluster of speed of vehicles')
plt.xlabel('distance feature')
plt.ylabel('speed feature')
#%%

kmeans = KMeans(n_clusters = 4 , init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)


plt.scatter(features[y_kmeans == 0,0], features[y_kmeans == 0,1] , s = 50 , c = 'red',label = 'urban and limited speed' )
plt.scatter(features[y_kmeans == 1,0], features[y_kmeans == 1,1] , s = 50 , c = 'blue', label = 'rural and limited speed')
plt.scatter(features[y_kmeans == 2,0], features[y_kmeans == 2,1] , s = 50 , c = 'green', label = 'rural and high speed ')
plt.scatter(features[y_kmeans == 3,0], features[y_kmeans ==3,1] , s = 50 , c = 'pink', label = 'urban and high speed')

plt.scatter(kmeans.cluster_centers_[: , 0], kmeans.cluster_centers_[: , 1],s = 200 , c = 'yellow',label = ' Centroids')


plt.title('cluster of speed of vehicles')
plt.xlabel('distance feature')
plt.ylabel('speed feature')
plt.legend()
plt.show()
from sklearn.datasets import make_blobs
import numpy as np 
import random as rand 

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x = []
y = []
for i in range(100):
    x.append(rand.random() * 100)
    y.append(rand.random() * 100)
plt.scatter(x, y)

data = list(zip(x, y))

kmeans = KMeans(n_clusters = 4)
kmeans.fit(data)
print(kmeans.cluster_centers_)


cluster_x = []
cluster_y = []
for i in kmeans.cluster_centers_:
    cluster_x.append(i[0])
    cluster_y.append(i[1])
plt.scatter(cluster_x, cluster_y, c = 'red')
plt.show()

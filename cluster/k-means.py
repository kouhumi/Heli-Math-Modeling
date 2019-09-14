from sklearn.datasets import make_blobs
import numpy as np 
import random as rand 

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x = []
y = []
for i in range(101):
    x.append(rand.random() * 100)
    y.append(rand.random() * 100)
plt.scatter(x, y)
plt.show()

data = list(zip(x, y))

kmeans = KMeans(n_clusters = 5)
kmeans.fit(data)

cluster_x = []
cluster_y = []
for i in kmeans.cluster_centers_:
    cluster_x.append(i[0])
    cluster_y.append(i[1])
plt.scatter(cluster_x, cluster_y, c = 'red')
plt.show()

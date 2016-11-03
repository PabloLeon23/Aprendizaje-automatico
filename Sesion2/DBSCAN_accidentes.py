
# coding: utf-8

# In[2]:

import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('../Data/Accidents.csv', 'r')
cs = csv.reader(f)
cs.next()

data = []
rows = []

for row in cs:
    lon = float(row[-2])
    lat = float(row[-1])
    data.append([lon, lat])
    rows.append(row)

X = np.asarray(data)


# In[3]:

# Plot accidents
fig, ax = plt.subplots()
plt.scatter(X[:,0], X[:,1], c='r', marker='o')
ax.grid(True)
plt.title('Accidentes en Bizkaia')
plt.show()


# In[4]:

# Compute k-nearest neighboors
from sklearn.neighbors import DistanceMetric, kneighbors_graph
dist = DistanceMetric.get_metric('euclidean')
matdist = dist.pairwise(X)

min_samples = 10
A = kneighbors_graph(X, min_samples, include_self=False)
Arr = A.toarray()

seq = []
for i in xrange(len(data)):
    for j in xrange(len(data)):
        if Arr[i][j] != 0:
            seq.append(matdist[i][j])
            
seq.sort()
plt.plot(seq)
plt.show()


# In[5]:

from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.0095, min_samples=10).fit(X)
unique_labels = set(db.labels_)
n_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)

print 'Número de clusters: ', n_clusters


# In[ ]:

# Validation/Evaluation
from sklearn import metrics
print "Silhoutte Coefficient: %0.3f" % metrics.silhouette_score(X, db.labels_)


# In[21]:

colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k != -1:
        class_member_mask = (db.labels_ == k)
        xy = X[db.labels_ == k]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markersize=6)
plt.title('Estimated number of clusters: %d' % n_clusters)
plt.show()


# In[6]:

#3. Write new data in a csv file
headers = ['causa', 'poblacion','fecha', 'hora', 'nivel', 'carretera', 
           'pk_inicial', 'pk_final', 'sentido', 'longitud', 'latitud',
          'zona']
with open('../Data/Accidents_zones_dbscan.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    for i in range(db.labels_.size):
        writer.writerow(rows[i]+[db.labels_[i]])


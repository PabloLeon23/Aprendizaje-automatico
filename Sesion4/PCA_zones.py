
# coding: utf-8

# In[1]:

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import csv


# In[2]:

# Zonas_kmeans.csv, Zonas_dbscan.csv
file_name = 'Zonas_dbscan.csv'


# In[3]:

f = open(file_name, 'r')
csvfile = csv.reader(f)
csvfile.next() #skip the headers
zonas = []

for zona in csvfile:
    zonas.append(zona)


# In[4]:

min_max_scaler = MinMaxScaler()
zonas = min_max_scaler.fit_transform([zona[1:] for zona in zonas])

pca_estimator = PCA(n_components = 2)
X_pca = pca_estimator.fit_transform(zonas)


# In[5]:

plt.scatter([x[0] for x in X_pca], [x[1] for x in X_pca])
plt.show()


# In[ ]:





# coding: utf-8

# In[21]:

import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('IncidenciasTDTGeo.csv', 'r')
cs = csv.reader(f)

data = []
rares = []

for row in cs:
    if row[0] == 'Accidente':
        lat = row[-1].rstrip()
        lon = row[-2].rstrip()
        if not '.' in lat:
            lat.insert(2, '.')
        if not '.' in lon:
            lon.insert(2, '.')
        
        lon = float(lon)
        lat = float(lat)
            
        if lon > -2.25:
            rares.append(row)
        else:
            data.append([lon, lat])

X = np.asarray(data)
            
print 'Accidente:', len(data)
print 'Raros:', len(rares)


# In[22]:


from sklearn.cluster import KMeans
from sklearn import metrics
                  
# plotting the generated data                  
import matplotlib.pyplot as plt

plt.scatter(X[:,0], X[:,1], c='r', marker='o')
plt.title('Accidentes en Bizkaia')
plt.show()


# In[ ]:


# Setting parameters (ad-hoc)
# parametros
init = 'random' 
iterations = 10 
max_iter = 300 
tol = 1e-04 
random_state = 0 


distortions = []
silhouettes = []

for i in range(20, 80):
    km = KMeans(i, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
    labels = km.fit_predict(X)
    distortions.append(km.inertia_)
    silhouettes.append(metrics.silhouette_score(X, labels))
    


# Plot distoritions    
plt.plot(range(20,80), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

# Plot Silhouette
plt.plot(range(20,80), silhouettes , marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Silohouette')
plt.show()
      


    



# In[ ]:




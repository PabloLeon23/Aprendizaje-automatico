
# coding: utf-8

# In[1]:

import csv
import matplotlib.pyplot as plt
import numpy as np


# <p style="font-family:courier;"> 1.Read the file of the zones of accidents labeled with the zone group obtained in the hierarchical clustering.</p>

# In[2]:

file_name_in = open('../Data/Zones_labels.csv')
zonas_csv = csv.reader(file_name_in)
features = zonas_csv.next()[1:-1]

data = []
target = []
for z in zonas_csv:
    data.append(z[1:-1])
    target.append(z[-1])
    
target_names = ['alto', 'bajo',  'medio']


# <p style="font-family:courier;">2. Create 100 random forests and calculate the average of the feature importance.</p>

# In[3]:

from sklearn.ensemble import RandomForestClassifier

its = 100
sums = np.zeros(len(features))

for _ in range(its):
    clf = RandomForestClassifier(n_jobs=-1)
    clf.fit(data, target)
    sums = sums + clf.feature_importances_
feature_importances = sums / its


# <p style="font-family:courier;">3. Print the feature relevance.</p>

# In[4]:

from tabulate import tabulate
table = zip(features, feature_importances)
print tabulate(table, headers = ['Feature', 'Relevance'])


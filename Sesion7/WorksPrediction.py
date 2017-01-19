
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import collections


# <p style="font-family:courier;">1. Read the files with the accidents of 2006 labeled with zones and the works of 2007, removing those accidents with a zone -1. </p>

# In[2]:

df_accidents = pd.read_csv('../Data/Accidents_zones_dbscan.csv')
df_accidents = df_accidents = df_accidents[['longitud', 'latitud', 'zona']]
df_accidents = df_accidents[df_accidents['zona'] != -1]

df_works = pd.read_csv('../Data/Works2007_filtered.csv')
df_works = df_works[['longitud', 'latitud']]


# <p style="font-family:courier;">2. Use a KNN model trained with the accidents of 2006, labeled with zones, to predict the zone of each 2007 work. The K parameter of the KNN model was calculated in Sesion5.</p>

# In[3]:

from sklearn import neighbors

K = 2
weight = 'distance'

clf = neighbors.KNeighborsClassifier(n_neighbors=K, weights=weight)
clf.fit(df_accidents[['longitud', 'latitud']], df_accidents['zona'])
Z = clf.predict(df_works)
Z_count = collections.Counter(Z)


# <p style="font-family:courier;">3. Add the number of works of a zone as a new zone feature and save the results in a csv file</p>

# In[4]:

import csv

f = open('../Data/Zones_labels.csv')
csv_file = csv.reader(f)
headers = csv_file.next()

zones_with_number_works = []
for row in csv_file:
    row.append(Z_count[int(row[0])])
    zones_with_number_works.append(row)
f.close()

headers.append('works')
f_out = open('../Data/Zones_with_number_works.csv', 'w')
csv_out = csv.writer(f_out)
csv_out.writerow(headers)
csv_out.writerows(zones_with_number_works)
f_out.close()


# <p style="font-family:courier;">4. Split the number of works in each zone in 3 groups: 'few', 'normal' and 'many'. In order to do that, we use a Kmeans algorithm with k=3.</p>

# In[5]:

from sklearn.cluster import KMeans

k = 3
init = 'k-means++' 
iterations = 10 
max_iter = 300

X = [[x[-1]] for x in zones_with_number_works]
km = KMeans(k, n_init=iterations, max_iter=max_iter, init=init)
labels = km.fit_predict(X)


# <p style="font-family:courier;">5. Add the label of number of works discretized: 'few', 'normal' and 'many' as a new feature of the zones. Save the results in a csv file</p>

# In[6]:

zones_with_discrete_works = []
for i, z in enumerate(zones_with_number_works):
    nz = z[:]
    if labels[i] == 1:
        nz[-1] = 'many'
    elif labels[i] == 0:
        nz[-1] = 'few'
    else:
        nz[-1] = 'normal'
    zones_with_discrete_works.append(nz)

f_out = open('../Data/Zones_with_discrete_works.csv', 'w')
csv_out = csv.writer(f_out)
csv_out.writerow(headers)
csv_out.writerows(zones_with_discrete_works)
f_out.close()


# <p style="font-family:courier;">6. Create and Decision Tree trained with the zones data and the quantity of works in each zone: few, normal or many. We set the maximum depth of the tree because the tree generated was very complex and not generalise well.</p>

# In[7]:

from sklearn import tree

features = headers[1:-1]
train = [zone[1:-1] for zone in zones_with_discrete_works]
target = [zone[-1] for zone in zones_with_discrete_works]

clf = tree.DecisionTreeClassifier(max_depth=2)
clf = clf.fit(train, target)


# <p style="font-family:courier;">7. Print the feature relevance in the Decision Tree.</p>

# In[8]:

from tabulate import tabulate

table = zip(features, clf.feature_importances_)
print tabulate(table, headers = ['Feature', 'Relevance'])


# <p style="font-family:courier;">8. Write a pdf file with the Decision Tree figure.</p>

# In[9]:

from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf, 
                     out_file = dot_data,
                     feature_names = features,
                     class_names = ['few', 'many', 'normal'],
                     filled = True,
                     rounded = True,
                     special_characters = True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf(path = 'zones.pdf')


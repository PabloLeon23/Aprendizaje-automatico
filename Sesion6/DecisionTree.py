
# coding: utf-8

# In[1]:

import csv
import matplotlib.pyplot as plt
import numpy as np


# In[2]:

file_name_in = open('../Data/Zones_labels.csv')
zonas_csv = csv.reader(file_name_in)
features = zonas_csv.next()[1:-1]

data = []
target = []
for z in zonas_csv:
    data.append(z[1:-1])
    target.append(z[-1])
    
target_names = ['bajo', 'medio',  'alto']


# In[3]:

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, target)


# In[4]:

from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf, out_file = dot_data,
                          feature_names = features,
                          class_names = target_names,
                          filled = True,
                          rounded = True,
                          special_characters = True)


# In[5]:

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf(path = 'zones.pdf')


# In[ ]:




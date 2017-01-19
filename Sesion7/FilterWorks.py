
# coding: utf-8

# In[1]:

import csv
import numpy as np


# <p style="font-family:courier;">Function that calculate if two work elements are refering to the same real work.</p>

# In[2]:

def is_same(w1, w2):
    date1, date2 = np.datetime64(w1[1] + ' ' + w1[2]), np.datetime64(w2[1] + ' ' + w2[2])
    lon1, lon2, lat1, lat2 = map(float, (w1[-2], w2[-2], w1[-1], w2[-1]))
    
    distance = np.sqrt((lon1-lon2)**2 + (lat1-lat2)**2)
    date_condition_strong = date2 - np.timedelta64(5, 'h') <= date1 <= date2 + np.timedelta64(5, 'h')
    date_condition_light = date2 - np.timedelta64(24, 'h') <= date1 <= date2 + np.timedelta64(24, 'h')
    spacial_condition = distance <= 0.05
    
    return date_condition_strong and spacial_condition or date_condition_light and distance == 0


# <p style="font-family:courier;">Open the file of the 2007 works.</p>

# In[3]:

f = open('../Data/Works2007.csv')
csv_file = csv.reader(f)
headers = csv_file.next()


# <p style="font-family:courier;">Iterate over the works and check if a work is repeated.</p>

# In[4]:

works = list()
for w1 in csv_file:
    eq = False
    for w2 in works:
        if is_same(w1, w2):
            eq = True
            break
    if not eq:
        works.append(w1)
f.close()


# <p style="font-family:courier;">Write the works filtered in a new file.</p>

# In[6]:

f_out = open('../Data/Works2007_filtered.csv', 'w')
csv_out = csv.writer(f_out)
csv_out.writerow(headers)
csv_out.writerows(works)


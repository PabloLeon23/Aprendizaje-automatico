
# coding: utf-8

# In[42]:

import csv
import matplotlib.pyplot as plt
import numpy as np


def equals(X, Y):
    lon1, lat1, date1, hour1 = float(X[-2]), float(X[-1]), X[2], X[3]
    lon2, lat2, date2, hour2 = float(Y[-2]), float(Y[-1]), Y[2], Y[3]
    date1 = np.datetime64(date1 + ' ' + hour1)
    date2 = np.datetime64(date2 + ' ' + hour2)
    
    spacial_condition = np.sqrt((lon1-lon2)**2 + (lat1-lat2)**2) <= 0.05
    date_condition = date2 - np.timedelta64(2, 'h') <= date1 <= date2 + np.timedelta64(2, 'h')
    
    return spacial_condition and date_condition


# In[43]:

f = open('../Data/Accidents.csv')
csv_file = csv.reader(f)
headers = csv_file.next()


# <p style="font-family:courier;">1. We evaluate if two accidents refer to the same accident</p>

# In[44]:

accidents = []
reps = 0

for row in csv_file:
    if accidents:
        eq = False
        for acc in accidents:
            if equals(row, acc):
                eq = True
                break
        if not eq:
            accidents.append(row)
        else:
            reps += 1
    else:
        accidents.append(row)

print 'Repatead accidents: ' + str(reps)


# In[46]:

with open('../Data/Accidents2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerows(accidents)



# coding: utf-8

# <p style="font-family:courier;">1. We evaluate if two accidents refer to the same accident</p>

# In[1]:

import csv
import matplotlib.pyplot as plt
import numpy as np


def equals(X, Y):
    condicion_espacial = np.sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2) <= 0.01
    condicion_temporal = X[2] - np.timedelta64(2, 'm') <= Y[2] and X[2] + np.timedelta64(2, 'm') >= Y[2]
    return condicion_espacial and condicion_temporal


# <p style="font-family:courier;">2. We read the accidents of the csv file IncidenciasTDTGeo and we remove the outliers</p>

# In[2]:

f = open('../Data/IncidenciasTDTGeo.csv', 'r')
cs = csv.reader(f)

data = []
rares = []
rows = []

lon_index = 13
lat_index = 14
date_index = 6

for row in cs:
    if row[0] == 'Accidente':
        lon = float(row[lon_index])
        lat = float(row[lat_index])
        date = np.datetime64(row[date_index])
       
        # Delete the outliers
        if lon > -2.25:
            rares.append(row)
        else:
            data.append([lon, lat, date])
            rows.append(row)

print 'Accidente:', len(data)
print 'Raros:', len(rares)


# <p style="font-family:courier;">3. We remove the repeated elements</p>

# In[3]:

new_rows = []
i = 0
while i < len(data):
    actual = data[i]
    repes = True
    while repes:
        i += 1
        if i == len(data) or not equals(actual, data[i]):
            repes = False
            i -= 1
    new_row = rows[i][4:6] + rows[i][6].split() + rows[i][7:12] + rows[i][13:]
    new_rows.append(new_row)
    i += 1


# <p style="font-family:courier;">4. We write new data in a csv file called Accidents</p>

# In[4]:

headers = ['causa', 'poblacion','fecha', 'hora', 'nivel', 'carretera', 'pk_inicial', 'pk_final', 'sentido', 'longitud', 'latitud']
with open('../Data/Accidents.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerows(new_rows)


# In[ ]:




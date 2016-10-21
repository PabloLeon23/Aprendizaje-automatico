import csv
import matplotlib.pyplot as plt
import numpy as np


# Evalua si dos accidentes se refieren al mismo
def equals(X, Y):
    condicion_espacial = np.sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2) <= 0.01
    condicion_temporal = X[2] - np.timedelta64(2, 'm') <= Y[2] and X[2] + np.timedelta64(2, 'm') >= Y[2]
    return condicion_espacial and condicion_temporal


# 1. Read the data from csv file
f = open('IncidenciasTDTGeo.csv', 'r')
cs = csv.reader(f)

data = []
rares = []

for row in cs:
    if row[0] == 'Accidente':
        lon = float(row[13])
        lat = float(row[14])
        date = np.datetime64(row[6])
        # Delete the outliers
        if lon > -2.25:
            rares.append(row)
        else:
            data.append([lon, lat, date])

print 'Accidente:', len(data)
print 'Raros:', len(rares)


# 2. Delete repited elements
new_data = []
i = 0
while i < len(data):
    actual = data[i]
    repes = True
    while repes:
        i += 1
        if i == len(data) or not equals(actual, data[i]):
            repes = False
            i -= 1
    new_data.append(actual[:-1])
    i += 1


#3. Write new data in a csv file
with open('Accidents.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(new_data)

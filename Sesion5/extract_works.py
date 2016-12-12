
# coding: utf-8

# <p style="font-family:courier;">1. Extract works from IncidenciasTDTGeo.</p>

# In[12]:

import csv

f = open('../Data/IncidenciasTDTGeo.csv', 'r')
cs = csv.reader(f)

new_rows = []
new_row= []

for row in cs:
    if row[0] == 'Obras':
            new_row = [row[5]] + row[6].split() + row[7:12] + row[13:]
            new_rows.append(new_row)
            

headers = [ 'poblacion','fecha', 'hora', 'nivel', 'carretera', 'pk_inicial', 'pk_final', 'sentido', 'longitud', 'latitud']
with open('../Data/Works.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerows(new_rows)


# In[ ]:




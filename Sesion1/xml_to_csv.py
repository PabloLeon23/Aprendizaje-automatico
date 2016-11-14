
# coding: utf-8

# <p style="font-family:courier;">1. We filter the incidences of XML occurring in Bizkaia and store them in a CSV called IncidenciasTDTGeo </p>

# In[4]:



import csv
import codecs

xml = codecs.open('../Data/IncidenciasTDTHist.xml', 'r', encoding='utf-8', errors='ignore')
X = xml.read().split('<incidenciaGeolocalizada>')[1:]

with open('../Data/IncidenciasTDTGeo.csv', 'w') as csvfile:
    fieldnames = ['tipo', 'autonomia', 'provincia', 'matricula', 'causa', 'poblacion',                'fechahora_ini', 'nivel', 'carretera', 'pk_inicial', 'pk_final',                'sentido', 'nombre', 'longitud', 'latitud']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    incidences = 0

    for row in X:
        if '<provincia>BIZKAIA' in row:
            data = {}
            row = row.split('><')[:-1]
            for campo in row:
                if '>' in campo:
                    ind1 = campo.index('>')
                    ind2 = campo.index('</')
                    nombre = campo[:ind1]
                    if 'tipo' in campo:
                        nombre = campo[1:ind1]
                    data[nombre] = campo[ind1+1:ind2]
                else:
                    data[campo[:-1]] = ''
            writer.writerow(data)
            incidences += 1
    print('Incidencias: ' + str(incidences))
    


# In[ ]:




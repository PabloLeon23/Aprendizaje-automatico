
# coding: utf-8

# In[1]:

import csv


# In[2]:

causa_i = 0
poblacion_i = 1
fecha_i = 2
hora_i = 3
nivel_i = 4
carretera_i = 5
pk_inicial_i = 6
pk_final_i = 7
zona_i = 11

zonas = dict()


# In[3]:

file_name_in = '../Data/Accidents_with_zones_dbscan.csv'


# <p style="font-family:courier;">1. We read the file Accidents_with_zones_dbscan that we have saved in file_name_in and created "Zonas". Zonas is a dictionary where the key is the zone and the content is a list of lists of accidents with their characteristics </p>

# In[4]:

f = open(file_name_in, 'r')
accidentes = csv.reader(f)
accidentes.next()

for accidente in accidentes:
    zona = int(accidente[zona_i])
    if zona != -1:
        if not zona in zonas:
            zonas[zona] = [accidente]
        else:
            zonas[zona].append(accidente)


# <p style="font-family:courier;">2. We identify the number of accidents based on a series of defined characteristics. The characteristics are tipe of accident, season of the year, hour and amount of traffic</p>

# In[5]:

n_accidentes = []

n_accidentes_por_alcance = [0] * len(zonas)
n_accidentes_por_atropello = [0] * len(zonas)
n_accidentes_por_salida = [0] * len(zonas)
n_accidentes_por_tijera_camion = [0] * len(zonas)
n_accidentes_por_vuelco = [0] * len(zonas)


dici_enero_feb = [0] * len(zonas)
marzo_abril_may = [0] * len(zonas)
jun_jul_agos = [0] * len(zonas)
sep_oct_nov = [0] * len(zonas)


manana=[0] * len(zonas)
tarde=[0] * len(zonas)



trafico_fluido=[0] * len(zonas)
trafico_lento=[0] * len(zonas)
trafico_muy_lento=[0] * len(zonas)
trafico_parado=[0] * len(zonas)

for zona in zonas:
    n_accidentes.append(len(zonas[zona]))
    for accidente in zonas[zona]:
        if accidente[causa_i] == 'Alcance':
            n_accidentes_por_alcance[zona] += 1
        if accidente[causa_i] == 'Atropello':
            n_accidentes_por_atropello[zona] += 1
        if accidente[causa_i] == 'Salida':
            n_accidentes_por_salida[zona] += 1
        if accidente[causa_i] == 'Vuelco':
            n_accidentes_por_vuelco[zona] += 1
        if accidente[causa_i] == 'Tijera camin':
            n_accidentes_por_tijera_camion[zona] += 1
        if '01' <= accidente[fecha_i][5:7] <= '02' or accidente[fecha_i][5:7] == '12':
            dici_enero_feb[zona] +=1 
        if '03' <= accidente[fecha_i][5:7] <= '05':
            marzo_abril_may[zona] +=1 
        if '06'<= accidente[fecha_i][5:7] <= '08':
            jun_jul_agos[zona] +=1 
        if '09'<= accidente[fecha_i][5:7] <= '11':
            sep_oct_nov[zona] +=1 
        if accidente[nivel_i] == 'Blanco':
            trafico_fluido[zona] +=1
        if accidente[nivel_i] == 'Amarillo':
            trafico_lento[zona] +=1
        if accidente[nivel_i] == 'Rojo':
            trafico_muy_lento[zona] +=1
        if accidente[nivel_i] == 'Negro':
            trafico_parado[zona] +=1
        if '00' <= accidente[hora_i][0:2] <'12':
            manana[zona] +=1
        if '12' <= accidente[hora_i][0:2] <='23':
            tarde[zona] +=1


# <p style="font-family:courier;">3. We add the list of new features to the zip and the header</p>

# In[6]:

rows = zip(zonas.keys(), n_accidentes, n_accidentes_por_alcance, n_accidentes_por_atropello,
          n_accidentes_por_salida, n_accidentes_por_tijera_camion, 
           n_accidentes_por_vuelco, dici_enero_feb, marzo_abril_may, 
           jun_jul_agos, sep_oct_nov, trafico_fluido, trafico_lento, 
           trafico_muy_lento, trafico_parado, manana, tarde)

headers = ['zona', 'accidentes', 'accidentes_alcance', 'accidentes_atropello',
          'accidentes_salida', 'accidentes_tijera_camion', 'accidentes_vuelco', 
            'accidentes_invierno', 'accidentes_primavera', 'accidentes_verano', 
           'accidentes_otoño', 'trafico_fluido', 'trafico_lento', 'trafico_muy_lento', 
          'trafico_parado','mañana(00:00-11:59)', 'tarde(12:00-23:59)']


# <p style="font-family:courier;">4. We write de zones features in a new csv file called Zonas_dbscan</p>

# In[7]:

file_name_out = '../Data/Zonas_dbscan.csv'

with open(file_name_out, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerows(rows)


# In[ ]:




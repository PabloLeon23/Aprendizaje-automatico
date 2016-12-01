Machine Learning class work:

1. First we convert de xml file with the traffic incidences in Bizkaia to a csv file. 
	Script: Sesion1/xml_to_csv.py
	Input: Data/IncidennciasTDTHist.xml
	Output: Data/IncidenciasTDTGeo.csv

2. We select the accidents incidences of the csv with all the incidences. 
	Script: Sesion2/extract_accidents.py
	Input: Data/IncidenciasTDTGeo.csv
	Output: Data/Accidents.csv

3. Next, we apply the DBScan algorithm for do clusters with the diferents accidents. Each cluster defines a zone of accidents.
	Script: Sesion2/DBSCAN_accidents.py
	Input: Data/Accidents.csv
	Output: Data/Accidents_with_zones_dbscan.csv

4. We apply the Spectral and K-means algorithms to accidents.csv. Each cluster defines a zone of accidents. We not consider the Spectral results because it haven't sense. 
	Script: Sesion3/Spectral-kmeans.py
	Input: Data/Accidents.csv
	Output: Data/Accidents_with_zones_kmeans.csv

5. We define different zones based on the features of the accidents that has ocurred in that zone.
	Script: Sesion4/extract_features_from_zones.py
	Input: Data/Accidents_with_zones_dbscan.csv, Data/Accidents_with_zones_kmeans.csv
	Output: Data/Zonas_dbscan.csv, Data/Zonas_kmeans.csv

6. We apply the PCA algorithm to the zones and do hierarchical clustering with the results. Next we define zone groups with their features.
	Script: Sesion4/PCA_hierarchical.py
	Input: Data/Zonas_dbscan.csv
	Output: Data/Grupos_zonas.csv

7. We modify the script of Step 2 for filter the accidents better.

 

* Each Script hava a Jupyter Notebook with comments.

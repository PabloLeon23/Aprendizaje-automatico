Machine Learning class work:

1. First we convert de xml file with the traffic incidences in Bizkaia to a csv file. <br/>
	Script: Sesion1/xml_to_csv.py<br/>
	Input: Data/IncidenciasTDTHist.xml<br/>
	Output: Data/IncidenciasTDTGeo.csv

2. We select the accidents incidences of the csv with all the incidences. <br/>
	Script: Sesion2/extract_accidents.py<br/>
	Input: Data/IncidenciasTDTGeo.csv<br/>
	Output: Data/Accidents.csv

3. Next, we apply the DBScan algorithm for do clusters with the diferents accidents. Each cluster defines a zone of accidents.<br/>
	Script: Sesion2/DBSCAN_accidents.py<br/>
	Input: Data/Accidents.csv<br/>
	Output: Data/Accidents_with_zones_dbscan.csv

4. We apply the Spectral and K-means algorithms to accidents.csv. Each cluster defines a zone of accidents. We not consider the Spectral results because it haven't sense. 
	Script: Sesion3/Spectral-kmeans.py <br/>
	Input: Data/Accidents.csv <br/>
	Output: Data/Accidents_with_zones_kmeans.csv <br/>

5. We define different zones based on the features of the accidents that has ocurred in that zone. <br/>
	Script: Sesion4/extract_features_from_zones.py <br/>
	Input: Data/Accidents_with_zones_dbscan.csv, Data/Accidents_with_zones_kmeans.csv <br/>
	Output: Data/Zonas_dbscan.csv, Data/Zonas_kmeans.csv <br/>

6. We apply the PCA algorithm to the zones and do hierarchical clustering with the results. Next we define zone groups with their features. <br/>
	Script: Sesion4/PCA_hierarchical.py <br/>
	Input: Data/Zonas_dbscan.csv <br/>
	Output: Data/Grupos_zonas.csv <br/>

7. We modify the script of Step 2 for filter the accidents better. So, we do all a second time with the accidents filtered.

8. We select the works of the initial incidences csv file for predict its zones.
	Scripts: Sesion5/extract_works.py <br/>
	Input: Data/IncidenciasTDTGeo.csv <br/>
	Output: Data/Works.csv<br/>

9. We create a KNN model trained with the accidents ant its zones for predict the zone of the works.
	Script: Sesion5/KNN-works.py <br/>
	Input: Data/Works.csv <br/>
	Output: Works_zones.csv<br/>

10. We predict the cluster group of each zone with a decision tree and extract the feature relevance. Because the implementation of decision trees has a random factor, we use Random Forest several times in order to improve the acuraccy of the feature relevance.
	Script: Sesion6/DecisionTree.py <br/>
	Script: Sesion6/RandomForest.py<br/>
	Input: Data/Zones_labels.csv <br/>

11. Next, we filter the works in 2007 for remove the repeated works.
	Script: Sesion7/FilterWorks.py<br/>
	Input: Data/Works2007.csv<br/>
	Output: Data/Works2007_filtered.csv<br/>
	

12. Next, we use the zones and the works of 2007 for create a prediction model with Decision Tree algorithm for predict the number of works in each zone.
	Script: Sesion7/WorksPrediction.py<br/>
	Input: /Data/Works2007_filtered.csv<br/>
	Output: /Data/Zones_with_number_works.csv, /Data/Zones_with_discrete_works.csv<br/>
	

 

* Each Script hava a Jupyter Notebook with comments.

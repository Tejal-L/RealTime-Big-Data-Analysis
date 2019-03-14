### module load python/gnu/2.7.11
### pip install --user uszipcode

import reverse_geocoder as rg
from uszipcode import SearchEngine
import numpy as np
import pandas as pd

######################################################

#		   traffic speed data cleaning               #  

######################################################

data = pd.read_csv('DOT_Traffic_Speeds_NBE.csv')
#data = pd.read_csv('sampleTrafficSpeed.csv')

def get_lat_long(value):
	return str(value).split()[0]

def get_MMYYYY(value):
	return value.split()[0]

def get_MMYYYY(value):
	return value.split("/")[0]+"/"+value.split("/")[2]

data['MMYYYY']=data['DATA_AS_OF'].apply(get_MMYYYY)


data['MMYYYY']  = data['MMYYYY'].apply(get_MMYYYY)

data['LAT_LONG']=data['LINK_POINTS'].apply(get_lat_long)

data = data[['MMYYYY','LAT_LONG','SPEED']]

search = SearchEngine(simple_zipcode=False)


def get_lat(value):
	n = str(value).strip().split(",")[0]
	return round(float(n),6) 

def get_long(value):
	n = str(value).strip().split(",")[1]
	return round(float(n),6) 


def lat_log_formatted(value):
	return str(get_lat(value))+","+str(get_long(value))

data['ZIPCODE']=data['LAT_LONG'].apply(lat_log_formatted)

newdf = data[['ZIPCODE']].copy()

newdf = newdf.drop_duplicates()

newdf.columns = ['LATLONG']



def get_zipCode(value):
	listOfPoints = str(value).split(",")
	if len(listOfPoints)>=2 :
		#Send Request
		result = search.by_coordinates(float(listOfPoints[0].strip()), float(listOfPoints[1].strip()), radius=30, returns=5)
		if len(result[0].zipcode) == 5 :
			return int(result[0].zipcode)
		else:
			return np.nan
	else:
		return np.nan

newdf['ZIPCODE'] = newdf['LATLONG'].apply(get_zipCode)

traffic = data[['MMYYYY', 'SPEED','ZIPCODE']].copy()
traffic.columns = ['MMYYYY','SPEED','LATLONG']
traffic.head(6)

temp_one = pd.Series(newdf['ZIPCODE'].tolist(), index=newdf['LATLONG'].tolist())
temp_one['40.82495,-73.836211']

def latlongToZip(value):
	return temp_one[value]

traffic['ZIPCODE'] = traffic['LATLONG'].apply(latlongToZip)
traffic = traffic.drop('LATLONG', axis = 1)
traffic.head(10)

avgtraffic = traffic.groupby(['MMYYYY','ZIPCODE']).agg({'SPEED':'mean'}).reset_index()

avgtraffic.columns = ['DATE', 'ZIPCODE','AVG_SPEED']

#df.groupby(['mth','id']).agg({'cost':'mean'}).reset_index()
	
###########################################################

##### 		CLUSTERING TRAFFIC DATA MONTH WISE 		#######

###########################################################
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
import MMYYYYtime 
import kneed
import pandas as pd
import sklearn



# newdf_count.to_csv('restaurantCluster.csv')

######################### JANUARY ####################


trafficJan2018 = avgtraffic.loc[avgtraffic['DATE'] == '01/2018']
trafficJan2018.shape    
mat = trafficJan2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficJan2018['label'] = labels

trafficJan2018 = trafficJan2018[['ZIPCODE','label']].copy()

trafficJan2018.to_csv("trafficJan2018.csv")

#####******************* FEBRUARY ********************

trafficFeb2018 = avgtraffic.loc[avgtraffic['DATE'] == '02/2018']
trafficFeb2018.shape    
mat = trafficFeb2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficFeb2018['label'] = labels
trafficFeb2018 = trafficFeb2018[['ZIPCODE','label']].copy()
trafficFeb2018.to_csv("trafficFeb2018.csv")


#####******************* MARCH ********************

trafficMar2018 = avgtraffic.loc[avgtraffic['DATE'] == '03/2018']
trafficMar2018.shape    
mat = trafficMar2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficMar2018['label'] = labels
trafficMar2018 = trafficMar2018[['ZIPCODE','label']].copy()
trafficMar2018.to_csv("trafficMar2018.csv")



#####******************* APRIL ********************

trafficApr2018 = avgtraffic.loc[avgtraffic['DATE'] == '04/2018']
trafficApr2018.shape    
mat = trafficApr2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficApr2018['label'] = labels
trafficApr2018 = trafficApr2018[['ZIPCODE','label']].copy()
trafficApr2018.to_csv("trafficApr2018.csv")



#####******************* MAY ********************

trafficMay2018 = avgtraffic.loc[avgtraffic['DATE'] == '05/2018']
trafficMay2018.shape    
mat = trafficMay2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficMay2018['label'] = labels
trafficMay2018 = trafficMay2018[['ZIPCODE','label']].copy()
trafficMay2018.to_csv("trafficMay2018.csv")



#####******************* JUNE ********************

trafficJun2018 = avgtraffic.loc[avgtraffic['DATE'] == '06/2018']
trafficJun2018.shape    
mat = trafficJun2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficJun2018['label'] = labels
trafficJun2018 = trafficJun2018[['ZIPCODE','label']].copy()
trafficJun2018.to_csv("trafficJun2018.csv")



#####******************* JULY ********************

trafficJul2018 = avgtraffic.loc[avgtraffic['DATE'] == '07/2018']
trafficJul2018.shape    
mat = trafficJul2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficJul2018['label'] = labels
trafficJul2018 = trafficJul2018[['ZIPCODE','label']].copy()
trafficJul2018.to_csv("trafficJul2018.csv")



#####******************* AUGUST ********************

trafficAug2018 = avgtraffic.loc[avgtraffic['DATE'] == '08/2018']
trafficAug2018.shape    
mat = trafficAug2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficAug2018['label'] = labels
trafficAug2018 = trafficAug2018[['ZIPCODE','label']].copy()
trafficAug2018.to_csv("trafficAug2018.csv")



#####******************* SEPTEMBER ********************

trafficSep2018 = avgtraffic.loc[avgtraffic['DATE'] == '09/2018']
trafficSep2018.shape    
mat = trafficSep2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficSep2018['label'] = labels
trafficSep2018 = trafficSep2018[['ZIPCODE','label']].copy()
trafficSep2018.to_csv("trafficSep2018.csv")


#####******************* OCTOBER ********************

trafficOct2018 = avgtraffic.loc[avgtraffic['DATE'] == '10/2018']
trafficOct2018.shape    
mat = trafficOct2018['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficOct2018['label'] = labels
trafficOct2018 = trafficOct2018[['ZIPCODE','label']].copy()
trafficOct2018.to_csv("trafficOct2018.csv")



##################################  2017 #######################################


######################### JANUARY ####################


trafficJan2017 = avgtraffic.loc[avgtraffic['DATE'] == '01/2017']
trafficJan2017.shape    
mat = trafficJan2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficJan2017['label'] = labels
trafficJan2017 = trafficJan2017[['ZIPCODE','label']].copy()
trafficJan2017.to_csv("trafficJan2017.csv")

#####******************* FEBRUARY ********************

trafficFeb2017 = avgtraffic.loc[avgtraffic['DATE'] == '02/2017']
trafficFeb2017.shape    
mat = trafficFeb2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficFeb2017['label'] = labels
trafficFeb2017 = trafficFeb2017[['ZIPCODE','label']].copy()
trafficFeb2017.to_csv("trafficFeb2017.csv")


#####******************* MARCH ********************

trafficMar2017 = avgtraffic.loc[avgtraffic['DATE'] == '03/2017']
trafficMar2017.shape    
mat = trafficMar2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficMar2017['label'] = labels
trafficMar2017 = trafficMar2017[['ZIPCODE','label']].copy()
trafficMar2017.to_csv("trafficMar2017.csv")



#####******************* APRIL ********************

trafficApr2017 = avgtraffic.loc[avgtraffic['DATE'] == '04/2017']
trafficApr2017.shape    
mat = trafficApr2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficApr2017['label'] = labels
trafficApr2017 = trafficApr2017[['ZIPCODE','label']].copy()
trafficApr2017.to_csv("trafficApr2017.csv")



#####******************* MAY ********************

trafficMay2017 = avgtraffic.loc[avgtraffic['DATE'] == '05/2017']
trafficMay2017.shape    
mat = trafficMay2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficMay2017['label'] = labels
trafficMay2017 = trafficMay2017[['ZIPCODE','label']].copy()
trafficMay2017.to_csv("trafficMay2017.csv")



#####******************* JUNE ********************

trafficJun2017 = avgtraffic.loc[avgtraffic['DATE'] == '06/2017']
trafficJun2017.shape    
mat = trafficJun2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficJun2017['label'] = labels
trafficJun2017 = trafficJun2017[['ZIPCODE','label']].copy()
trafficJun2017.to_csv("trafficJun2017.csv")



#####******************* JULY ********************

trafficJul2017 = avgtraffic.loc[avgtraffic['DATE'] == '07/2017']
trafficJul2017.shape    
mat = trafficJul2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficJul2017['label'] = labels
trafficJul2017 = trafficJul2017[['ZIPCODE','label']].copy()
trafficJul2017.to_csv("trafficJul2017.csv")



#####******************* AUGUST ********************

trafficAug2017 = avgtraffic.loc[avgtraffic['DATE'] == '08/2017']
trafficAug2017.shape    
mat = trafficAug2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficAug2017['label'] = labels
trafficAug2017 = trafficAug2017[['ZIPCODE','label']].copy()
trafficAug2017.to_csv("trafficAug2017.csv")



#####******************* SEPTEMBER ********************

trafficSep2017 = avgtraffic.loc[avgtraffic['DATE'] == '09/2017']
trafficSep2017.shape    
mat = trafficSep2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficSep2017['label'] = labels
trafficSep2017 = trafficSep2017[['ZIPCODE','label']].copy()
trafficSep2017.to_csv("trafficSep2017.csv")


#####******************* OCTOBER ********************

trafficOct2017 = avgtraffic.loc[avgtraffic['DATE'] == '10/2017']
trafficOct2017.shape    
mat = trafficOct2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficOct2017['label'] = labels
trafficOct2017 = trafficOct2017[['ZIPCODE','label']].copy()
trafficOct2017.to_csv("trafficOct2017.csv")



#####******************* NOVEMBER ********************

trafficNov2017 = avgtraffic.loc[avgtraffic['DATE'] == '11/2017']
trafficNov2017.shape    
mat = trafficNov2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficNov2017['label'] = labels
trafficNov2017 = trafficNov2017[['ZIPCODE','label']].copy()
trafficNov2017.to_csv("trafficNov2017.csv")

#####******************* DECEMBER ********************

trafficDec2017 = avgtraffic.loc[avgtraffic['DATE'] == '12/2017']
trafficDec2017.shape    
mat = trafficDec2017['AVG_SPEED'].values
import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

trafficDec2017['label'] = labels
trafficDec2017 = trafficDec2017[['ZIPCODE','label']].copy()
trafficDec2017.to_csv("trafficDec2017.csv")


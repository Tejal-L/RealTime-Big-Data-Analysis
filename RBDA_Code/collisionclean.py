# We are trying to find the optimum number of clusters for each month 
# We will be using these number of clusters on other dataset as well to 
# perform union

import pandas as pd
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
import datetime 
import kneed


data = pd.read_csv('NYPD_Motor_Vehicle_Collisions-2.csv')

data.head(5)

data.shape

filtered_df = data[data['ZIP CODE'].notnull()]

dfOne = filtered_df[['DATE','ZIP CODE']]

dfOne.head(5)

dfOne.shape

dfOne['DATE'] = pd.to_datetime(dfOne['DATE'])

dfOne['DATE'] = dfOne['DATE'].dt.strftime('%m%Y')


newdf = dfOne

newdf = newdf.groupby(['DATE','ZIP CODE']).DATE.agg('count').to_frame('COUNTS').reset_index()

newdf.shape

newdf.head(5)

newdf.drop(newdf.head(1).index, inplace=True)

newdf.shape

newdf.head(5)


#############################

import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
###############################################

collJan2018 = newdf.loc[newdf['DATE']=='012018']
col1 = collJan2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJan2018['label'] = collabels

collJan2018.to_csv('collJan2018.csv')

##############################################

collFeb2018 = newdf.loc[newdf['DATE']=='022018']
col1 = collFeb2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collFeb2018['label'] = collabels

collFeb2018.to_csv('collFeb2018.csv')

##############################################

collMar2018 = newdf.loc[newdf['DATE']=='032018']
col1 = collMar2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collMar2018['label'] = collabels

collMar2018.to_csv('collMar2018.csv')

##############################################

collApr2018 = newdf.loc[newdf['DATE']=='042018']
col1 = collApr2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collApr2018['label'] = collabels

collApr2018.to_csv('collApr2018.csv')


##############################################

collMay2018 = newdf.loc[newdf['DATE']=='052018']
col1 = collMay2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collMay2018['label'] = collabels

collMay2018.to_csv('collMay2018.csv')


##############################################

collJun2018 = newdf.loc[newdf['DATE']=='062018']
col1 = collJun2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJun2018['label'] = collabels

collJun2018.to_csv('collJun2018.csv')
##############################################

collJul2018 = newdf.loc[newdf['DATE']=='072018']
col1 = collJul2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJul2018['label'] = collabels

collJul2018.to_csv('collJul2018.csv')

##############################################

collAug2018 = newdf.loc[newdf['DATE']=='082018']
col1 = collAug2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collAug2018['label'] = collabels

collAug2018.to_csv('collAug2018.csv')
##############################################

collSep2018 = newdf.loc[newdf['DATE']=='092018']
col1 = collSep2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collSep2018['label'] = collabels

collSep2018.to_csv('collSep2018.csv')


##############################################

collOct2018 = newdf.loc[newdf['DATE']=='102018']
col1 = collOct2018['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collOct2018['label'] = collabels

collOct2018.to_csv('collOct2018.csv')


###############   2017 ###############################

collJan2017 = newdf.loc[newdf['DATE']=='012017']
col1 = collJan2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJan2017['label'] = collabels

collJan2017.to_csv('collJan2017.csv')

##############################################

collFeb2017 = newdf.loc[newdf['DATE']=='022017']
col1 = collFeb2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collFeb2017['label'] = collabels

collFeb2017.to_csv('collFeb2017.csv')

##############################################

collMar2017 = newdf.loc[newdf['DATE']=='032017']
col1 = collMar2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collMar2017['label'] = collabels

collMar2017.to_csv('collMar2017.csv')

##############################################

collApr2017 = newdf.loc[newdf['DATE']=='042017']
col1 = collApr2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collApr2017['label'] = collabels

collApr2017.to_csv('collApr2017.csv')


##############################################

collMay2017 = newdf.loc[newdf['DATE']=='052017']
col1 = collMay2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collMay2017['label'] = collabels

collMay2017.to_csv('collMay2017.csv')


##############################################

collJun2017 = newdf.loc[newdf['DATE']=='062017']
col1 = collJun2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJun2017['label'] = collabels

collJun2017.to_csv('collJun2017.csv')
##############################################

collJul2017 = newdf.loc[newdf['DATE']=='072017']
col1 = collJul2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJul2017['label'] = collabels

collJul2017.to_csv('collJul2017.csv')

##############################################

collAug2017 = newdf.loc[newdf['DATE']=='082017']
col1 = collAug2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collAug2017['label'] = collabels

collAug2017.to_csv('collAug2017.csv')
##############################################

collSep2017 = newdf.loc[newdf['DATE']=='092017']
col1 = collSep2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collSep2017['label'] = collabels

collSep2017.to_csv('collSep2017.csv')


##############################################

collOct2017 = newdf.loc[newdf['DATE']=='102017']
col1 = collOct2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collOct2017['label'] = collabels

collOct2017.to_csv('collOct2017.csv')




##############################################

collNov2017 = newdf.loc[newdf['DATE']=='112017']
col1 = collNov2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collNov2017['label'] = collabels

collNov2017.to_csv('collNov2017.csv')



##############################################

collDec2017 = newdf.loc[newdf['DATE']=='122017']
col1 = collDec2017['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collDec2017['label'] = collabels

collDec2017.to_csv('collDec2017.csv')



############################ 2016 #####################


###############################################

collJan2016 = newdf.loc[newdf['DATE']=='012016']
col1 = collJan2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJan2016['label'] = collabels

collJan2016.to_csv('collJan2016.csv')

##############################################

collFeb2016 = newdf.loc[newdf['DATE']=='022016']
col1 = collFeb2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collFeb2016['label'] = collabels

collFeb2016.to_csv('collFeb2016.csv')

##############################################

collMar2016 = newdf.loc[newdf['DATE']=='032016']
col1 = collMar2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collMar2016['label'] = collabels

collMar2016.to_csv('collMar2016.csv')

##############################################

collApr2016 = newdf.loc[newdf['DATE']=='042016']
col1 = collApr2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collApr2016['label'] = collabels

collApr2016.to_csv('collApr2016.csv')


##############################################

collMay2016 = newdf.loc[newdf['DATE']=='052016']
col1 = collMay2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collMay2016['label'] = collabels

collMay2016.to_csv('collMay2016.csv')


##############################################

collJun2016 = newdf.loc[newdf['DATE']=='062016']
col1 = collJun2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJun2016['label'] = collabels

collJun2016.to_csv('collJun2016.csv')
##############################################

collJul2016 = newdf.loc[newdf['DATE']=='072016']
col1 = collJul2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collJul2016['label'] = collabels

collJul2016.to_csv('collJul2016.csv')

##############################################

collAug2016 = newdf.loc[newdf['DATE']=='082016']
col1 = collAug2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collAug2016['label'] = collabels

collAug2016.to_csv('collAug2016.csv')
##############################################

collSep2016 = newdf.loc[newdf['DATE']=='092016']
col1 = collSep2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collSep2016['label'] = collabels

collSep2016.to_csv('collSep2016.csv')


##############################################

collOct2016 = newdf.loc[newdf['DATE']=='102016']
col1 = collOct2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collOct2016['label'] = collabels

collOct2016.to_csv('collOct2016.csv')




##############################################

collNov2016 = newdf.loc[newdf['DATE']=='112016']
col1 = collNov2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collNov2016['label'] = collabels

collNov2016.to_csv('collNov2016.csv')



##############################################

collDec2016 = newdf.loc[newdf['DATE']=='122016']
col1 = collDec2016['COUNTS'].values

km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(col1.reshape(-1,1))

collabels = km.labels_
collabels

collDec2016['label'] = collabels

collDec2016.to_csv('collDec2016.csv')


























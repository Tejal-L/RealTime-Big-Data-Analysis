#Third Dataset - Restaurant dataset
#Here, we have cleaned the data to generate a dataframe that displays
#Number of restaurant in a particular zipcode
#We intend to union this data with other dataset clusters
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
import pandas as pd
import sklearn

df = pd.read_csv('restaurant_data_set_2-2.csv')
df.head(3)

df =  df[['CAMIS', 'ZIPCODE']].copy()
#newdf= df.filter(['ZIPCODE'], axis=1)
df =  df.drop_duplicates()
newdf = df[['ZIPCODE']].copy()

newdf.head(2)

newdf['count'] = 1

newdf_count =newdf.groupby(["ZIPCODE"])["ZIPCODE"].count().reset_index(name="count")



################################ CLUSTERING #############3

mat = newdf_count['count'].values

import sklearn
km = sklearn.cluster.KMeans(n_clusters=3)
km.fit(mat.reshape(-1,1))
labels = km.labels_
labels

newdf_count['label'] = labels
#newdf_count.to_csv('restaurantCluster.csv')

restaurantCluster = newdf_count




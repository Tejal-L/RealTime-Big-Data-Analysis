##############INTERSECTION OF COLLISION AND TRAFFIC AND RESTAURANT DATA #################




################ JAN 2018 #################

df1= pd.read_csv('Jan2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficJan2018 = pd.read_csv("trafficJan2018.csv")
df2 = trafficJan2018[['ZIPCODE', 'label']].copy()

resultJan2018 = pd.merge(df1, df2, how = 'inner')
resultJan2018.shape
resultJan2018.to_csv('Jan2018_all3.csv')


################ FEB 2018 #################

df1= pd.read_csv('Feb2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficFeb2018 = pd.read_csv("trafficFeb2018.csv")

df2 = trafficFeb2018[['ZIPCODE', 'label']].copy()
df2.shape

resultFeb2018 = pd.merge(df1, df2, how = 'inner')
resultFeb2018.shape
resultFeb2018.to_csv('Feb2018_all3.csv')
resultFeb2018.shape


################ MARCH 2018 #################

df1= pd.read_csv('Mar2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficMar2018 = pd.read_csv("trafficMar2018.csv")

df2 = trafficMar2018[['ZIPCODE', 'label']].copy()

resultMar2018 = pd.merge(df1, df2, how = 'inner')
resultMar2018.shape
resultMar2018.to_csv('Mar2018_all3.csv')

################ APRIL 2018 #################
df1= pd.read_csv('Apr2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficApr2018 = pd.read_csv("trafficApr2018.csv")

df2 = trafficApr2018[['ZIPCODE', 'label']].copy()

resultApr2018 = pd.merge(df1, df2, how = 'inner')
resultApr2018.shape
resultApr2018.to_csv('Apr2018_all3.csv')

################ MAY 2018 #################
df1= pd.read_csv('May2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficMay2018 = pd.read_csv("trafficMay2018.csv")

df2 = trafficMay2018[['ZIPCODE', 'label']].copy()

resultMay2018 = pd.merge(df1, df2, how = 'inner')
resultMay2018.shape
resultMay2018.to_csv('May2018_all3.csv')

################ JUN 2018 #################
df1= pd.read_csv('Jun2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficJun2018 = pd.read_csv("trafficJun2018.csv")

df2 = trafficJun2018[['ZIPCODE', 'label']].copy()

resultJun2018 = pd.merge(df1, df2, how = 'inner')
resultJun2018.shape
resultJun2018.to_csv(Jun2018_all3.csv)

################ JULY 2018 #################
df1= pd.read_csv('Jul2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficJul2018 = pd.read_csv("trafficJul2018.csv")

df2 = trafficJul2018[['ZIPCODE', 'label']].copy()

resultJul2018 = pd.merge(df1, df2, how = 'inner')
resultJul2018.shape
resultJun2018.to_csv('Jul2018_all3.csv')


################ AUGUST 2018 #################
df1= pd.read_csv('Aug2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficAug2018 = pd.read_csv("trafficAug2018.csv")

df2 = trafficAug2018[['ZIPCODE', 'label']].copy()

collAug2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collAug2018[['ZIPCODE', 'label']].copy()

resultAug2018 = pd.merge(df1, df2, how = 'inner')
resultAug2018.shape
resultAug2018.to_csv('Aug2018_all3.csv')


################ SEPTEMBER 2018 #################
df1= pd.read_csv('Sep2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficSep2018 = pd.read_csv("trafficSep2018.csv")

df2 = trafficSep2018[['ZIPCODE', 'label']].copy()

collSep2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collSep2018[['ZIPCODE', 'label']].copy()

resultSep2018 = pd.merge(df1, df2, how = 'inner')
resultSep2018.shape
resultSep2018.to_csv('Sep2018_all3.csv')

################ OCTOBER 2018 #################
df1= pd.read_csv('Oct2018CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficOct2018 = pd.read_csv("trafficOct2018.csv")

df2 = trafficOct2018[['ZIPCODE', 'label']].copy()

resultOct2018 = pd.merge(df1, df2, how = 'inner')
resultOct2018.shape
resultOct2018.to_csv('Oct2018_all3.csv')


############### 2017 ########################


################ JAN 2017 #################

df1= pd.read_csv('Jan2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficJan2017 = pd.read_csv("trafficJan2017.csv")
df2 = trafficJan2017[['ZIPCODE', 'label']].copy()

resultJan2017 = pd.merge(df1, df2, how = 'inner')
resultJan2017.shape
resultJan2017.to_csv('Jan2017_all3.csv')


################ FEB 2017 #################

df1= pd.read_csv('Feb2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficFeb2017 = pd.read_csv("trafficFeb2017.csv")

df2 = trafficFeb2017[['ZIPCODE', 'label']].copy()
resultFeb2017 = pd.merge(df1, df2, how = 'inner')
resultFeb2017.shape
resultFeb2017.to_csv('Feb2017_all3.csv')


################ MARCH 2017 #################

df1= pd.read_csv('Mar2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficMar2017 = pd.read_csv("trafficMar2017.csv")

df2 = trafficMar2017[['ZIPCODE', 'label']].copy()

resultMar2017 = pd.merge(df1, df2, how = 'inner')
resultMar2017.shape
resultMar2017.to_csv('Mar2017_all3.csv')

################ APRIL 2017 #################
df1= pd.read_csv('Apr2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficApr2017 = pd.read_csv("trafficApr2017.csv")

df2 = trafficApr2017[['ZIPCODE', 'label']].copy()

resultApr2017 = pd.merge(df1, df2, how = 'inner')
resultApr2017.shape
resultApr2017.to_csv('Apr2017_all3.csv')

################ MAY 2017 #################
df1= pd.read_csv('May2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficMay2017 = pd.read_csv("trafficMay2017.csv")

df2 = trafficMay2017[['ZIPCODE', 'label']].copy()

resultMay2017 = pd.merge(df1, df2, how = 'inner')
resultMay2017.shape
resultMay2017.to_csv('May2017_all3.csv')

################ JUN 2017 #################
df1= pd.read_csv('Jun2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficJun2017 = pd.read_csv("trafficJun2017.csv")

df2 = trafficJun2017[['ZIPCODE', 'label']].copy()

resultJun2017 = pd.merge(df1, df2, how = 'inner')
resultJun2017.shape
resultJun2017.to_csv(Jun2017_all3.csv)

################ JULY 2017 #################
df1= pd.read_csv('Jul2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape

trafficJul2017 = pd.read_csv("trafficJul2017.csv")

df2 = trafficJul2017[['ZIPCODE', 'label']].copy()

resultJul2017 = pd.merge(df1, df2, how = 'inner')
resultJul2017.shape
resultJun2017.to_csv('Jul2017_all3.csv')


################ AUGUST 2017 #################
df1= pd.read_csv('Aug2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficAug2017 = pd.read_csv("trafficAug2017.csv")

df2 = trafficAug2017[['ZIPCODE', 'label']].copy()

collAug2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collAug2017[['ZIPCODE', 'label']].copy()

resultAug2017 = pd.merge(df1, df2, how = 'inner')
resultAug2017.shape
resultAug2017.to_csv('Aug2017_all3.csv')


################ SEPTEMBER 2017 #################
df1= pd.read_csv('Sep2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficSep2017 = pd.read_csv("trafficSep2017.csv")

df2 = trafficSep2017[['ZIPCODE', 'label']].copy()

collSep2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collSep2017[['ZIPCODE', 'label']].copy()

resultSep2017 = pd.merge(df1, df2, how = 'inner')
resultSep2017.shape
resultSep2017.to_csv('Sep2017_all3.csv')

################ OCTOBER 2017 #################
df1= pd.read_csv('Oct2017CollRest.csv')
df1 = df1[['ZIPCODE','label']].copy()
df1.shape


trafficOct2017 = pd.read_csv("trafficOct2017.csv")

df2 = trafficOct2017[['ZIPCODE', 'label']].copy()

resultOct2017 = pd.merge(df1, df2, how = 'inner')
resultOct2017.shape
resultOct2017.to_csv('Oct2017_all3.csv')

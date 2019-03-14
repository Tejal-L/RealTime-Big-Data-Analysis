##############INTERSECTION OF COLLISION AND TRAFFIC DATA #################


df1= restaurantCluster[['ZIPCODE','label']].copy()
df1.shape

################ JAN 2018 #################

trafficJan2018 = pd.read_csv("trafficJan2018.csv")

df2 = trafficJan2018[['ZIPCODE', 'label']].copy()

resultJan2018 = pd.merge(df1, df2, how = 'inner')
resultJan2018.shape
resultJan2018.to_csv('Jan2018CollTraf.csv')


################ FEB 2018 #################

trafficFeb2018 = pd.read_csv("trafficFeb2018.csv")

df2 = trafficFeb2018[['ZIPCODE', 'label']].copy()
resultFeb2018 = pd.merge(df1, df2, how = 'inner')
resultFeb2018.shape
resultFeb2018.to_csv('Feb2018CollTraf.csv')


################ MARCH 2018 #################

trafficMar2018 = pd.read_csv("trafficMar2018.csv")

df2 = trafficMar2018[['ZIPCODE', 'label']].copy()

resultMar2018 = pd.merge(df1, df2, how = 'inner')
resultMar2018.shape
resultMar2018.to_csv('Mar2018CollTraf.csv')

################ APRIL 2018 #################

trafficApr2018 = pd.read_csv("trafficApr2018.csv")

df2 = trafficApr2018[['ZIPCODE', 'label']].copy()

resultApr2018 = pd.merge(df1, df2, how = 'inner')
resultApr2018.shape
resultApr2018.to_csv('Apr2018CollTraf.csv')

################ MAY 2018 #################
trafficMay2018 = pd.read_csv("trafficMay2018.csv")

df2 = trafficMay2018[['ZIPCODE', 'label']].copy()

resultMay2018 = pd.merge(df1, df2, how = 'inner')
resultMay2018.shape
resultMay2018.to_csv('May2018CollTraf.csv')

################ JUN 2018 #################

trafficJun2018 = pd.read_csv("trafficJun2018.csv")

df2 = trafficJun2018[['ZIPCODE', 'label']].copy()

resultJun2018 = pd.merge(df1, df2, how = 'inner')
resultJun2018.shape
resultJun2018.to_csv(Jun2018CollTraf.csv)

################ JULY 2018 #################
trafficJul2018 = pd.read_csv("trafficJul2018.csv")

df2 = trafficJul2018[['ZIPCODE', 'label']].copy()

resultJul2018 = pd.merge(df1, df2, how = 'inner')
resultJul2018.shape
resultJun2018.to_csv('Jul2018CollTraf.csv')


################ AUGUST 2018 #################

trafficAug2018 = pd.read_csv("trafficAug2018.csv")

df2 = trafficAug2018[['ZIPCODE', 'label']].copy()

collAug2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collAug2018[['ZIPCODE', 'label']].copy()

resultAug2018 = pd.merge(df1, df2, how = 'inner')
resultAug2018.shape
resultAug2018.to_csv('Aug2018CollTraf.csv')


################ SEPTEMBER 2018 #################
trafficSep2018 = pd.read_csv("trafficJun2018.csv")

df2 = trafficSep2018[['ZIPCODE', 'label']].copy()

collSep2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collSep2018[['ZIPCODE', 'label']].copy()

resultSep2018 = pd.merge(df1, df2, how = 'inner')
resultSep2018.shape
resultSep2018.to_csv('Sep2018CollTraf.csv')

################ OCTOBER 2018 #################

trafficOct2018 = pd.read_csv("trafficOct2018.csv")

df2 = trafficOct2018[['ZIPCODE', 'label']].copy()

resultOct2018 = pd.merge(df1, df2, how = 'inner')
resultOct2018.shape
resultOct2018.to_csv('Oct2018CollTraf.csv')

###################### 2017 #################################

##############INTERSECTION OF COLLISION AND RESTAURANT DATA #################


df1= restaurantCluster[['ZIPCODE','label']].copy()
df1.shape

################ JAN 2017 #################

trafficJan2017 = pd.read_csv("trafficJan2017.csv")

df2 = trafficJan2017[['ZIPCODE', 'label']].copy()

resultJan2017 = pd.merge(df1, df2, how = 'inner')
resultJan2017.shape
resultJan2017.to_csv('Jan2017CollTraf.csv')


################ FEB 2017 #################
trafficFeb2017 = pd.read_csv("trafficFeb2017.csv")

df2 = trafficFeb2017[['ZIPCODE', 'label']].copy()

resultFeb2017 = pd.merge(df1, df2, how = 'inner')
resultFeb2017.shape
resultFeb2017.to_csv('Feb2017CollTraf.csv')


################ MARCH 2017 #################

trafficMar2017 = pd.read_csv("trafficMar2017.csv")

df2 = trafficMar2017[['ZIPCODE', 'label']].copy()

resultMar2017 = pd.merge(df1, df2, how = 'inner')
resultMar2017.shape
resultMar2017.to_csv('Mar2017CollTraf.csv')

################ APRIL 2017 #################

trafficApr2017 = pd.read_csv("trafficApr2017.csv")

df2 = trafficApr2017[['ZIPCODE', 'label']].copy()

resultApr2017 = pd.merge(df1, df2, how = 'inner')
resultApr2017.shape
resultApr2017.to_csv('Apr2017CollTraf.csv')

################ MAY 2017 #################

trafficMay2017 = pd.read_csv("trafficMay2017.csv")

df2 = trafficMay2017[['ZIPCODE', 'label']].copy()

resultMay2017 = pd.merge(df1, df2, how = 'inner')
resultMay2017.shape
resultMay2017.to_csv('May2017CollTraf.csv')

################ JUN 2017 #################


trafficJun2017 = pd.read_csv("trafficJun2017.csv")

df2 = trafficJun2017[['ZIPCODE', 'label']].copy()


resultJun2017 = pd.merge(df1, df2, how = 'inner')
resultJun2017.shape
resultJun2017.to_csv(Jun2017CollTraf.csv)

################ JULY 2017 #################

trafficJul2017 = pd.read_csv("trafficJul2017.csv")

df2 = trafficJul2017[['ZIPCODE', 'label']].copy()

resultJul2017 = pd.merge(df1, df2, how = 'inner')
resultJul2017.shape
resultJun2017.to_csv('Jul2017CollTraf.csv')


################ AUGUST 2017 #################

trafficAug2017 = pd.read_csv("trafficAug2017.csv")

df2 = trafficAug2017[['ZIPCODE', 'label']].copy()

resultAug2017 = pd.merge(df1, df2, how = 'inner')
resultAug2017.shape
resultAug2017.to_csv('Aug2017CollTraf.csv')


################ SEPTEMBER 2017 #################

trafficSep2017 = pd.read_csv("trafficSep2017.csv")

df2 = trafficSep2017[['ZIPCODE', 'label']].copy()

resultSep2017 = pd.merge(df1, df2, how = 'inner')
resultSep2017.shape
resultSep2017.to_csv('Sep2017CollTraf.csv')

################ OCTOBER 2017 #################

trafficOct2017 = pd.read_csv("trafficOct2017.csv")

df2 = trafficOct2017[['ZIPCODE', 'label']].copy()

resultOct2017 = pd.merge(df1, df2, how = 'inner')
resultOct2017.shape
resultOct2017.to_csv('Oct2017CollTraf.csv')


################ NOVEMBER 2017 #################

trafficNov2017 = pd.read_csv("trafficNov2017.csv")

df2 = trafficNov2017[['ZIPCODE', 'label']].copy()

resultNov2017 = pd.merge(df1, df2, how = 'inner')
resultNov2017.shape
resultNov2017.to_csv('Nov2017CollTraf.csv')

################ DECEMBER 2017 #################

trafficDec2017 = pd.read_csv("trafficDec2017.csv")

df2 = trafficDec2017[['ZIPCODE', 'label']].copy()

resultDec2017 = pd.merge(df1, df2, how = 'inner')
resultDec2017.shape
resultDec2017.to_csv('Dec2017CollTraf.csv')


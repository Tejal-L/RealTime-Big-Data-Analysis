##############INTERSECTION OF COLLISION AND RESTAURANT DATA #################


df1= restaurantCluster[['ZIPCODE','label']].copy()
df1.shape

################ JAN 2018 #################

collJan2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJan2018[['ZIPCODE', 'label']].copy()

resultJan2018 = pd.merge(df1, df2, how = 'inner')
resultJan2018.shape
resultJan2018.to_csv('Jan2018CollRest.csv')


################ FEB 2018 #################

collFeb2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collFeb2018[['ZIPCODE', 'label']].copy()

resultFeb2018 = pd.merge(df1, df2, how = 'inner')
resultFeb2018.shape
resultFeb2018.to_csv('Feb2018CollRest.csv')


################ MARCH 2018 #################

collMar2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collMar2018[['ZIPCODE', 'label']].copy()

resultMar2018 = pd.merge(df1, df2, how = 'inner')
resultMar2018.shape
resultMar2018.to_csv('Mar2018CollRest.csv')

################ APRIL 2018 #################

collApr2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collApr2018[['ZIPCODE', 'label']].copy()

resultApr2018 = pd.merge(df1, df2, how = 'inner')
resultApr2018.shape
resultApr2018.to_csv('Apr2018CollRest.csv')

################ MAY 2018 #################

collMay2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collMay2018[['ZIPCODE', 'label']].copy()

resultMay2018 = pd.merge(df1, df2, how = 'inner')
resultMay2018.shape
resultMay2018.to_csv('May2018CollRest.csv')

################ JUN 2018 #################

collJun2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJun2018[['ZIPCODE', 'label']].copy()

resultJun2018 = pd.merge(df1, df2, how = 'inner')
resultJun2018.shape
resultJun2018.to_csv(Jun2018CollRest.csv)

################ JULY 2018 #################

collJul2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJul2018[['ZIPCODE', 'label']].copy()

resultJul2018 = pd.merge(df1, df2, how = 'inner')
resultJul2018.shape
resultJun2018.to_csv('Jul2018CollRest.csv')


################ AUGUST 2018 #################

collAug2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collAug2018[['ZIPCODE', 'label']].copy()

resultAug2018 = pd.merge(df1, df2, how = 'inner')
resultAug2018.shape
resultAug2018.to_csv('Aug2018CollRest.csv')


################ SEPTEMBER 2018 #################

collSep2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collSep2018[['ZIPCODE', 'label']].copy()

resultSep2018 = pd.merge(df1, df2, how = 'inner')
resultSep2018.shape
resultSep2018.to_csv('Sep2018CollRest.csv')

################ OCTOBER 2018 #################

collOct2018.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collOct2018[['ZIPCODE', 'label']].copy()

resultOct2018 = pd.merge(df1, df2, how = 'inner')
resultOct2018.shape
resultOct2018.to_csv('Oct2018CollRest.csv')

###################### 2017 #################################

##############INTERSECTION OF COLLISION AND RESTAURANT DATA #################


df1= restaurantCluster[['ZIPCODE','label']].copy()
df1.shape

################ JAN 2017 #################

collJan2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJan2017[['ZIPCODE', 'label']].copy()

resultJan2017 = pd.merge(df1, df2, how = 'inner')
resultJan2017.shape
resultJan2017.to_csv('Jan2017CollRest.csv')


################ FEB 2017 #################

collFeb2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collFeb2017[['ZIPCODE', 'label']].copy()

resultFeb2017 = pd.merge(df1, df2, how = 'inner')
resultFeb2017.shape
resultFeb2017.to_csv('Feb2017CollRest.csv')


################ MARCH 2017 #################

collMar2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collMar2017[['ZIPCODE', 'label']].copy()

resultMar2017 = pd.merge(df1, df2, how = 'inner')
resultMar2017.shape
resultMar2017.to_csv('Mar2017CollRest.csv')

################ APRIL 2017 #################

collApr2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collApr2017[['ZIPCODE', 'label']].copy()

resultApr2017 = pd.merge(df1, df2, how = 'inner')
resultApr2017.shape
resultApr2017.to_csv('Apr2017CollRest.csv')

################ MAY 2017 #################

collMay2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collMay2017[['ZIPCODE', 'label']].copy()

resultMay2017 = pd.merge(df1, df2, how = 'inner')
resultMay2017.shape
resultMay2017.to_csv('May2017CollRest.csv')

################ JUN 2017 #################

collJun2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJun2017[['ZIPCODE', 'label']].copy()

resultJun2017 = pd.merge(df1, df2, how = 'inner')
resultJun2017.shape
resultJun2017.to_csv(Jun2017CollRest.csv)

################ JULY 2017 #################

collJul2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJul2017[['ZIPCODE', 'label']].copy()

resultJul2017 = pd.merge(df1, df2, how = 'inner')
resultJul2017.shape
resultJun2017.to_csv('Jul2017CollRest.csv')


################ AUGUST 2017 #################

collAug2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collAug2017[['ZIPCODE', 'label']].copy()

resultAug2017 = pd.merge(df1, df2, how = 'inner')
resultAug2017.shape
resultAug2017.to_csv('Aug2017CollRest.csv')


################ SEPTEMBER 2017 #################

collSep2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collSep2017[['ZIPCODE', 'label']].copy()

resultSep2017 = pd.merge(df1, df2, how = 'inner')
resultSep2017.shape
resultSep2017.to_csv('Sep2017CollRest.csv')

################ OCTOBER 2017 #################

collOct2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collOct2017[['ZIPCODE', 'label']].copy()

resultOct2017 = pd.merge(df1, df2, how = 'inner')
resultOct2017.shape
resultOct2017.to_csv('Oct2017CollRest.csv')


################ NOVEMBER 2017 #################

collNov2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collNov2017[['ZIPCODE', 'label']].copy()

resultNov2017 = pd.merge(df1, df2, how = 'inner')
resultNov2017.shape
resultNov2017.to_csv('Nov2017CollRest.csv')

################ DECEMBER 2017 #################

collDec2017.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collDec2017[['ZIPCODE', 'label']].copy()

resultDec2017 = pd.merge(df1, df2, how = 'inner')
resultDec2017.shape
resultDec2017.to_csv('Dec2017CollRest.csv')


###################### 2016 #########################

##############INTERSECTION OF COLLISION AND RESTAURANT DATA #################


df1= restaurantCluster[['ZIPCODE','label']].copy()
df1.shape

################ JAN 2016 #################

collJan2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJan2016[['ZIPCODE', 'label']].copy()

resultJan2016 = pd.merge(df1, df2, how = 'inner')
resultJan2016.shape
resultJan2016.to_csv('Jan2016CollRest.csv')


################ FEB 2016 #################

collFeb2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collFeb2016[['ZIPCODE', 'label']].copy()

resultFeb2016 = pd.merge(df1, df2, how = 'inner')
resultFeb2016.shape
resultFeb2016.to_csv('Feb2016CollRest.csv')


################ MARCH 2016 #################

collMar2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collMar2016[['ZIPCODE', 'label']].copy()

resultMar2016 = pd.merge(df1, df2, how = 'inner')
resultMar2016.shape
resultMar2016.to_csv('Mar2016CollRest.csv')

################ APRIL 2016 #################

collApr2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collApr2016[['ZIPCODE', 'label']].copy()

resultApr2016 = pd.merge(df1, df2, how = 'inner')
resultApr2016.shape
resultApr2016.to_csv('Apr2016CollRest.csv')

################ MAY 2016 #################

collMay2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collMay2016[['ZIPCODE', 'label']].copy()

resultMay2016 = pd.merge(df1, df2, how = 'inner')
resultMay2016.shape
resultMay2016.to_csv('May2016CollRest.csv')

################ JUN 2016 #################

collJun2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJun2016[['ZIPCODE', 'label']].copy()

resultJun2016 = pd.merge(df1, df2, how = 'inner')
resultJun2016.shape
resultJun2016.to_csv(Jun2016CollRest.csv)

################ JULY 2016 #################

collJul2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collJul2016[['ZIPCODE', 'label']].copy()

resultJul2016 = pd.merge(df1, df2, how = 'inner')
resultJul2016.shape
resultJun2016.to_csv('Jul2016CollRest.csv')


################ AUGUST 2016 #################

collAug2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collAug2016[['ZIPCODE', 'label']].copy()

resultAug2016 = pd.merge(df1, df2, how = 'inner')
resultAug2016.shape
resultAug2016.to_csv('Aug2016CollRest.csv')


################ SEPTEMBER 2016 #################

collSep2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collSep2016[['ZIPCODE', 'label']].copy()

resultSep2016 = pd.merge(df1, df2, how = 'inner')
resultSep2016.shape
resultSep2016.to_csv('Sep2016CollRest.csv')

################ OCTOBER 2016 #################

collOct2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collOct2016[['ZIPCODE', 'label']].copy()

resultOct2016 = pd.merge(df1, df2, how = 'inner')
resultOct2016.shape
resultOct2016.to_csv('Oct2016CollRest.csv')


################ NOVEMBER 2016 #################

collNov2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collNov2016[['ZIPCODE', 'label']].copy()

resultNov2016 = pd.merge(df1, df2, how = 'inner')
resultNov2016.shape
resultNov2016.to_csv('Nov2016CollRest.csv')

################ DECEMBER 2016 #################

collDec2016.columns  = ['DATE','ZIPCODE','COUNTS','label']
df2 = collDec2016[['ZIPCODE', 'label']].copy()

resultDec2016 = pd.merge(df1, df2, how = 'inner')
resultDec2016.shape
resultDec2016.to_csv('Dec2016CollRest.csv')























# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:15:32 2019

@author: Jmore
"""

#Pandas

#Series
import pandas as pd
import numpy as np

ser1 = pd.Series([10,20,30],['A','B','C'])
print("Series -1 as data and labels: \n{}\n".format(ser1))

py_dict = {'A':10,'K':22,'I':90}
ser2 = pd.Series(py_dict)
print("Series -2 as dict: \n{}\n".format(ser2))

print(ser1 + ser2) #print(ser1 - ser2) print(ser1 * ser2)
# It will take the common labels and performs the operations on those data points

#Data frame
df1 = pd.DataFrame(np.random.randn(3,3),['L1','L2','L3'],['C1','C2','C3'])
#first arg - data, second - labels, third - columns
print(df1)

print("Selecting column1: \n{}\n".format(df1['C1']))
print("Selecting a list of columns [1 and 2]: \n{}\n".format(df1[['C1','C2']]))

print("Selecting row1: \n{}\n".format(df1.loc['L1']))
print("Selecting a list of rows 1 and 2: \n{}\n".format(df1.loc[['L1','L2']]))

print("Selecting custom rows and columns: \n{}\n".format(df1.loc[['L1','L2']][['C1','C2']]))
#first we will filter the rows/labels and then we filter the columns

#Creating a new column/Series

df1['New'] = df1['C1'] + df1['C2']
print(df1)

#Dropping a column/Series
df1.drop('New',axis=1) #because it is a column axis will be 1
#to drop a row the axis will be 0(its 0 by default)
df1.drop('L1',axis=0)
#and it is not inplace, because by default inplace = False. 
df1.drop('L1',axis=0,inplace=True)

#loc, iloc for selecting rows
print(df1.loc['L2'])
print(df1.iloc[0])

#Conditional selection of data frames
print(df1 > 0) #Returns a boolean data frame containing True/False with respect to the condition specified for all the data points
print(df1[df1['C1']>0])

#Conditional
df1[df1['New']>0][:] #Selecting all the columns
df1[df1['New']>0][['C1','C2','C3']] #Specifying a list of columns

#Multiple conditions
#df1[(df1['New']>0) and (df1['C2']>1)] # we cannot use 'and' here
df1[(df1['New']>0) & (df1['C2']>1)] # we have to use '&'
df1[(df1['New']>0) | (df1['C2']>1)] # similarly for 'or' use | 


#resetting the index/labels
#we will get a column 'index' with the previous indexes and indexes will be reset to 0,1,2...
df1.reset_index(inplace=False)

df1['States'] = ['CA','AUS']
df1.set_index('States',inplace=False)
#set_index doesn't retain the values(previous index values) to a new column, so it is better to reset_index and preserve the indexes before we reset

#Multa index and index hierarchy
#First we need to build a outer and inner indexings
multi_ind = (zip(['G1']*3 + ['G2']*3, ['1','2','3']*2))
higher_ind = pd.MultiIndex.from_tuples(multi_ind)
df2 = pd.DataFrame(data = np.random.randn(6,3), index = higher_ind, columns = ['A','B','C'])
print(df2.loc['G2'])
print(df2.loc['G2'].loc['1'])
#if we see 
print(df2.index.names) #we will get a frozen list 
df2.index.names = ['Groups','Num']
print(df2.index.names) #we will get a frozen list 
print("df2: \n{}".format(df2))

#Cross section - If we want to pull data from inner index, it is useful
print("Data for the index Num = 1: \n{}".format(df2.xs('1',level='Num')))


#########################################
#####  MISSING DATA
#########################################
df3_dict = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df3 = pd.DataFrame(df3_dict)
print("df3: \n {}".format(df3))
df3.dropna() #Default axis=0 so removes the NaN rows
df3.dropna(axis=1) #Now it removes the NaN columns

df3.fillna(value = "Fill Value")
df3.dropna(thresh=2) #Threshold, drop NaN vaules only when at least threshold 2


################################
##### GROUP BY 
################################

data_df4 = {'Company':['Google','FB','MSFT','Google','FB','MSFT'],
        'Employee':['John','Sanket','Rakesh','Manmeet','Jai','Jadhav'],
        'Sales':[10,20,30,40,50,60]}

df4 = pd.DataFrame(data_df4)
print("df4: \n {}".format(df4))
print(df4.groupby('Company').sum())
print(df4.groupby('Company').mean())
print(df4.groupby(['Company','Employee']).sum())
print(df4.groupby(['Company','Employee']).sum().loc['Google']) #grop by company and employee then find the aggregate sum for the Google org.
print(df4.groupby('Company').describe()) # we will get count, mean, std, min, max, percentile
print(df4.groupby('Company').describe().transpose().loc['FB'])

############################################
##### Concatenation 
## In order to glue the data frames..

#res_df = pd.concat([df1,df2,df3], axis = 0) #concatenate along the rows
#res_df = pd.concat([df1,df2,df3], axis = 1) #concatenate along the columns

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
        'A': ['A0','A1','A2','A3'],
        'B': ['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
        'C': ['C0','C1','C2','C3'],
        'D': ['D0','D1','D2','D3']})

#### Merging
## Merge function allows you to merge DataFrames together using a similar logic as SQL Merge
pd.merge(left,right,how='inner',on='key')

####Joining
#Join is a convenient method for combining the columns of two potentially different-indexed DataFrames into a single data frame.
#If you want to merge two data frames based off one of their columns use Merge
#but the join functionality comes off the data frame 
left = pd.DataFrame({ 'A': ['A0','A1','A2'], 'B': ['B0','B1','B2']},
                      index = ['K0','K1','K2'])

right = pd.DataFrame({ 'C': ['C0','C1','C2'], 'D': ['D0','D1','D2']},
                      index = ['K0','K2','K3'])

left.join(right,how='inner')
left.join(right,how='left')
left.join(right,how='right')


######################################################################
################## Operations
###################################################

df6 = pd.DataFrame({'col1':[1,2,3,4],
       'col2':[444,555,666,444],
       'col3':['abc','def','ghi','jkl']})

df6.head()

#If we want to find the unique values of a column, use unique() method on the series, and it returns a Numpy array
df6['col2'].unique() #returns a Numpy array of unique values
df6['col2'].nunique() #returns no.of unique values
df6['col2'].value_counts() #returns a table of values and their counts

###Conditional Selection
df6[(df6['col1'] > 1) & (df6['col2'] == 444)]

## Apply function
df6.apply(lambda x: x*2)  ### applies to all columns
df6['col2'].apply(lambda x: x*2) #only to a specific column
df6['col3'].apply(len) # this becomes handy when it comes to trigger inbuilt methods to all the elements of the data frames

#If we want to drop a column say col1 
df6.drop('col1',axis=1,inplace=False)
df6.columns #returns a lis of columns
df6.index #returns a list of index 

### Sorting

df6.sort_values('col2')
# same as df6.sort_values(by = 'col2')

df7 = pd.DataFrame({ 'A': ['foo']*3 + ['bar']*3,
                    'B': ['one']*2 + ['two']*2 + ['one']*2,
                    'C': ['x','y']*3,
                    'D':[1,3,2,5,4,1]        })

df7.pivot_table(values='D', index=['A','B'],columns='C')#,aggfunc='mean' by default 
# and this index [A,B] will creates a multi-level index



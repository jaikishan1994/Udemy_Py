# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:02:40 2020

@author: Jmore
"""

#Pandas exercise
import pandas as pd

sal = pd.read_csv('D:/Python/Udemy\Salaries.csv')
print(sal.head())
sal.info() #to check how many entries are there in the data frame

sal = sal[sal['BasePay']!='Not Provided'] #Remove the strings
sal['BasePay'] = sal['BasePay'].apply(float) #TypeCase the data points before apply any standard functions

print("Average BasePay: {}".format(sal['BasePay'].mean())) #Average BasePay
print("Maximum Overtime Pay: {}".format(sal['OvertimePay'].apply(float).max()))
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']) #Job title of an employee
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])

print(sal[sal['TotalPay'] == sal['TotalPay'].max()]) #Highest paid employee
print(sal[sal['TotalPay'] == sal['TotalPay'].min()]) #Lowest paid employee
##### A quick other alternative to check it with the index is
sal.loc[sal['TotalPay'].idxmax()]

#argmax() returns index of the max element of the Numpy array or series
#sal.loc[sal['TotalPay'].argmax()]

print(sal.groupby('Year').mean()['BasePay']) #Avg BasePay for all the employees per year(2011-2014)

print(sal['JobTitle'].nunique()) #No.of unique job titles
print(sal['JobTitle'].value_counts().head(5))

#How many job titles were represented by only one person in 2013
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

#How many people have the word 'chief' in their job title
def check_chief_in_jobtitle(jobtitle):
    if 'chief' in jobtitle.lower().split():
        return True
    else:
        return False

print(sal['JobTitle'].apply(lambda x: check_chief_in_jobtitle(x))) #returns a boolean data frame 
print(sum(sal['JobTitle'].apply(lambda x: check_chief_in_jobtitle(x)))) #returns the sum


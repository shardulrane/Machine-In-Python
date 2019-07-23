# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:53:57 2019

@author: SHARDUL
"""

import numpy as np  
import pandas as pd

df=pd.read_csv('rating.csv')
df=df.drop(columns='Unnamed: 0')

df.groupby('Report_ID')['Rating'].mean().sort_values(ascending=False).head()  
df.groupby('Report_ID')['Rating'].count().sort_values(ascending=False).head()  
ratings_mean_count = pd.DataFrame(df.groupby('Report_ID')['Rating'].mean())  
ratings_mean_count['rating_counts'] = pd.DataFrame(df.groupby('Report_ID')['Rating'].count())
ratings_mean_count.head()

"""import matplotlib.pyplot as plt  
import seaborn as sns  
sns.set_style('dark')  

plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
ratings_mean_count['rating_counts'].hist(bins=50)    

plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
ratings_mean_count['Rating'].hist(bins=50)

plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
sns.jointplot(x='Rating', y='rating_counts', data=ratings_mean_count, alpha=0.4) 
"""
user_report_rating = df.pivot_table(index='Name', columns='Report_ID', values='Rating')  
#user_report_rating.head()

given_report_ratings = user_report_rating[477] 
#given_report_ratings

reports_like_given = user_report_rating.corrwith(given_report_ratings)

corr_given = pd.DataFrame(reports_like_given, columns=['Correlation'])  
corr_given.dropna(inplace=True)  
#corr_given  

corr_given = corr_given.join(ratings_mean_count['rating_counts'])  
#corr_given.head()  
print("Reports Recommended for The Selected Report")
print(corr_given[corr_given ['rating_counts']>50].sort_values('Correlation', ascending=False).head())
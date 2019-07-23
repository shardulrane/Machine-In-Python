# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:58:07 2019

@author: SHARDUL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime, timedelta


min_year=2014
max_year=datetime.now().year
start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)
ts=list()
for i in range(2000):
    random_date = start + (end - start) * random.random()
    ts.append(random_date)
def gen_datetime(min_year=2015, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


df=pd.read_csv('rand_names.csv')
data=pd.DataFrame()
data1=pd.DataFrame()
na=list(df['Name'])
naa=random.choices(na,k=2000)
df1=pd.read_csv('names.csv')
ow=list(df1['Owner'])
row=random.choices(ow,k=2000)
data1['User']=naa
data1['Profile']=row
data1['Timestamp']=ts
df.to_csv('profile_hits.csv')
own=pd.read_csv('reports.csv')
own = own.drop(columns="Unnamed: 0")
own_name=list(own['Owner'])
rid=list(own['Report_Id'])
rrid=random.choices(rid,k=5000)
owner=list()
hits=list()
for i in range(0,2000):
    hits.append(random.randint(0,200))
df['Hits']=hits
df['No_Of_Views']=viw    
data['Timestamp']=ts
data['Report_Id']=rrid
data['Owner']=owner
df.to_csv('views.csv')
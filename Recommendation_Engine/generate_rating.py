# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:13:28 2019

@author: SHARDUL
"""

import numpy as np  
import pandas as pd
import random

from datetime import datetime, timedelta


min_year=2014
max_year=datetime.now().year
start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)
ts=list()
for i in range(50000):
    random_date = start + (end - start) * random.random()
    ts.append(random_date)
def gen_datetime(min_year=2015, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()



df=pd.read_csv("reports.csv")
df1=pd.DataFrame()
rid=list(df['Report_Id'])
ow=list(df['Owner'])
gene=list(df['Industry'] +"|"+ df['Technology'])
df1=pd.DataFrame()
names=list(df1['name'])*5
#for 
rr=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]
rrid=list()
gene1=list()
rat=list()
own=list()
for i in range(0,50000):
    tt=random.randint(0,499)
    rrid.append(rid[tt])
    gene1.append(gene[tt])
    own.append(ow[tt])
    rat.append(random.choice(rr))
df1['Name']=names
df1['Report_ID']=rrid
df1['Owner']=own
df1['Type']=gene1
df1['Rating']=rat
df1['Timestamp']=ts
df1.to_csv('rating.csv')
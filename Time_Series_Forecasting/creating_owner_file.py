# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:42:28 2019

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

str1=str("Healthcare    Pharmaceuticals    Chemicals & Materials    Manufacturing    Construction    Energy and Power    Energy and Power    Construction    Chemicals and Materials    Automotive    Telecom    Food    Beverage    FMCG    Retails    Banking    Finance    Insurance    Defense    Government    Agriculture    Robotics    Semiconductor    Software    Hardware    Automation    Process Control    Technology    Mining    Education    Advertising    Marketing    Aerospace    Transportation    Packaging    Medical Devices    Theraputic Area    Biotechnology    Medical Imaging    Healthcare Services    Hospital Management    Diagnostics    Laboratory Equipment    Drug by Therapeutic Area    Oncology Drugs    Drug Delivery    Pharmanceutical Manufacturing    Biopharmaceuticals    Drug Discovery    Vitamins & Dietary Suppliments    Clinical Trials    Chemicals    Plastics    Composites    Adhesives & Sealants    Metals & Minerals    Metals & Minerals    Rubber    Glass    Textiles    Ceramics    Nanomaterials    Advanced Materials    Machinery    Machine Parts    Engineering    Building Materials    Construction    HVAC (Heating, Ventilation, & Air Conditioning)    Material Handling Equipment    Manufacturing & Industry    Industrial Automation    Logistics")
industry=str1.split("    ")
str2=str("3D Printing     Artificial Intelligence     Big Data & Analytics     Blockchain     Connectivity     Digitization     Internet of Things(IoT)     Nano Technology     Robotics     Smart Infrastructure     Smart Manufacturing     Wearable     Self Driving Cars     AR/VR     Drones     Cloud Computing")
technology=str2.split("     ")

df=pd.read_csv('owner.csv')
df = df.drop(columns="Unnamed: 0")
rindust=random.choices(industry, k=500)
rtech=random.choices(technology, k=500)
df['Industry']=rindust
df['Technology']=rtech    
cgr=list()
ms=list()
for i in range(0,500):
    cgr.append(random.randint(-10, 300))
    ms.append(random.randint(100, 1000))
df['CAGR']=cgr
df['Market_Size']=ms
df.to_csv('reports.csv')
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:00:09 2019

@author: SHARDUL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt
import seaborn as sns; sns.set()
import statsmodels.api as sm
import warnings
import itertools

plt.style.use('fivethirtyeight')
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['text.color'] = 'k'

df=pd.read_csv('final_trans_hist.csv')
#df=df.drop(columns="Unnamed: 0.1")
df=df.drop(columns="Unnamed: 0")
ss=input("Enter The Owner Name To find the Revenue Predictions: ")
own=df.loc[df['Owner'] == ss]
own['Time'] = pd.to_datetime(own['Time'])

own.dtypes
own['Time'].min(), own['Time'].max()

own.isnull().sum()

own = own.groupby('Time')['Cost'].sum().reset_index()

own = own.set_index('Time')
own.index
y = own['Cost'].resample('MS').mean()
y.fillna(0, inplace=True)
y['2018':]
#to understand the pattern
#y.plot(figsize=(15, 6))
#plt.show()


#going for further decomosition
#from pylab import rcParams
#rcParams['figure.figsize'] = 18, 8
#decomposition = sm.tsa.seasonal_decompose(y, model='additive')
#fig = decomposition.plot()
#plt.show()

#Using ARIMA Model
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
#print('Examples of parameter combinations for Seasonal ARIMA...')
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
#print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
#print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
pak_param=0
seaonal=0
maic=9999999
#fitting the model into your Y
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            if results.aic<maic:
                maic=results.aic
                pak_param=param
                seaonal=param_seasonal
                
#            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

mod = sm.tsa.statespace.SARIMAX(y,
                                order=pak_param,
                                seasonal_order=seaonal,
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
#print(results.summary().tables[1])

#results.plot_diagnostics(figsize=(16, 8))
#plt.show()

#checking pred with old data

pred = results.get_prediction(start=pd.to_datetime('2017-08-01'), dynamic=False)
pred_ci = pred.conf_int()
#ax = y['2014':].plot(label='observed')
#pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
#ax.fill_between(pred_ci.index,
#                pred_ci.iloc[:, 0],
#                pred_ci.iloc[:, 1], color='k', alpha=.2)
#ax.set_xlabel('Date')
#ax.set_ylabel('Revenue Generated')
#plt.legend()
#plt.show()ags

y_forecasted = pred.predicted_mean
y_truth = y['2017-01-01':]
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))
#less the RMS number greater the accuracy
#predictions with visulization

pred_uc = results.get_forecast(steps=50)
pred_ci = pred_uc.conf_int()
ax = y.plot(label='observed', figsize=(10, 5))
pred_uc.predicted_mean.plot(ax=ax, label='Revenue Generation Forecast Based On The Past Record')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Revenue Generated')
plt.legend()
plt.show()

print(pred_uc)
print(pred_uc.conf_int())
print("Predicted Vaues")
print(pred_uc.predicted_mean)

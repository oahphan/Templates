#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:10:38 2019

@author: MyOanh
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from mpl_finance import candlestick_ohlc 
import matplotlib.dates as mdates

#Get data
start = datetime(2015, 1, 1)
end = datetime(2017, 1, 1)

vcb_stock = pd.read_csv('./excel_vcb.csv')
dhg_stock = pd.read_csv('./excel_dhg.csv')
msn_stock = pd.read_csv('./excel_msn.csv')

#Clean data
vcb_stock = vcb_stock.drop('<Ticker>',axis=1)
dhg_stock = dhg_stock.drop('<Ticker>',axis=1)
msn_stock = msn_stock.drop('<Ticker>',axis=1)
#Rename
vcb = vcb_stock.rename({'<DTYYYYMMDD>':'Date', '<Open>':'Open', '<High>':'High', '<Low>':'Low', '<Close>':'Close', '<Volume>':'Volume'}, axis=1)
dhg = dhg_stock.rename({'<DTYYYYMMDD>':'Date', '<Open>':'Open', '<High>':'High', '<Low>':'Low', '<Close>':'Close', '<Volume>':'Volume'}, axis=1)
msn = msn_stock.rename({'<DTYYYYMMDD>':'Date', '<Open>':'Open', '<High>':'High', '<Low>':'Low', '<Close>':'Close', '<Volume>':'Volume'}, axis=1)

#Format date
vcb['Date'] = vcb['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
dhg['Date'] = dhg['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
msn['Date'] = msn['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))

####Lchon ngay cho du lieu
vcb_nhap = vcb[(vcb['Date'] > start) & (vcb['Date'] < end)]
# set ngay lam index
vcb_nhap.set_index('Date',inplace=True)
# visualising
fig1 = plt.figure(figsize = (12, 6))
plt.title('Open')
vcb_nhap['Open'].plot(label = 'VCB')
plt.legend()

fig2 = plt.figure(figsize = (12, 6))
plt.title('Volume')
vcb_nhap['Volume'].plot(label = 'VCB')
plt.legend()

vcb_nhap['Total Traded'] = vcb_nhap['Open'] * vcb_nhap['Volume']

fig3 = plt.figure(figsize = (12, 6))
plt.title('Total Traded')
vcb_nhap['Total Traded'].plot(label = 'VCB')
plt.legend()

########################candle stick 10D resample######################
### Method 1: use matplotlib
# VCB

vcb_ohlc = vcb_nhap['Close'].resample('10D').ohlc()
vcb_volume = vcb_nhap['Volume'].resample('10D').sum()

vcb_ohlc.reset_index(inplace=True)
vcb_ohlc['Date']=vcb_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan =5, colspan= 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan =1, colspan= 1, sharex = ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, vcb_ohlc.values, width=2, colorup = 'g')
ax2.fill_between(vcb_volume.index.map(mdates.date2num),vcb_volume.values, 0)
plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)
#plt.show()
plt.savefig('candle-vcb.png')

# DHG
dhg_nhap = dhg[(dhg['Date'] > start) & (dhg['Date'] < end)]
dhg_nhap.set_index('Date',inplace=True)
# visualising
fig1 = plt.figure(figsize = (12, 6))
plt.title('Open')
dhg_nhap['Open'].plot(label = 'DHG')
plt.legend()

fig2 = plt.figure(figsize = (12, 6))
plt.title('Volume')
dhg_nhap['Volume'].plot(label = 'DHG')
plt.legend()

dhg_nhap['Total Traded'] = dhg_nhap['Open'] * dhg_nhap['Volume']
fig3 = plt.figure(figsize = (12, 6))
plt.title('Total Traded')
dhg_nhap['Total Traded'].plot(label = '')
plt.legend()

dhg_ohlc = dhg_nhap['Close'].resample('10D').ohlc()
dhg_volume = dhg_nhap['Volume'].resample('10D').sum()
dhg_ohlc.reset_index(inplace=True)
dhg_ohlc['Date']=dhg_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan =5, colspan= 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan =1, colspan= 1, sharex = ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, dhg_ohlc.values, width=2, colorup = 'g')
ax2.fill_between(dhg_volume.index.map(mdates.date2num),dhg_volume.values, 0)
plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)
#plt.show()
plt.savefig('candle-dhg.png')

# MSN
msn_nhap = msn[(msn['Date'] > start) & (msn['Date'] < end)]
msn_nhap.set_index('Date',inplace=True)

# visualising
fig1 = plt.figure(figsize = (12, 6))
plt.title('Open')
msn_nhap['Open'].plot(label = 'MSN')
plt.legend()

fig2 = plt.figure(figsize = (12, 6))
plt.title('Volume')
msn_nhap['Volume'].plot(label = 'MSN')
plt.legend()

msn_nhap['Total Traded'] = msn_nhap['Open'] * msn_nhap['Volume']
fig3 = plt.figure(figsize = (12, 6))
plt.title('Total Traded')
msn_nhap['Total Traded'].plot(label = 'MSN')
plt.legend()

msn_ohlc = msn_nhap['Close'].resample('10D').ohlc()
msn_volume = msn_nhap['Volume'].resample('10D').sum()
msn_ohlc.reset_index(inplace=True)
msn_ohlc['Date']=msn_ohlc['Date'].map(mdates.date2num)
ax1 = plt.subplot2grid((6,1), (0,0), rowspan =5, colspan= 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan =1, colspan= 1, sharex = ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, msn_ohlc.values, width=2, colorup = 'g')
ax2.fill_between(msn_volume.index.map(mdates.date2num),msn_volume.values, 0)
# Format time.
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
ax2.xaxis_date()
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
# Beautify the x-labels
plt.gcf().autofmt_xdate()   
plt.autoscale(tight=True)
# Name of figure
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('MASAN')
#plt.show()
plt.savefig('candle-msn.png')


###############################CANDLE STICK 1D#################################
start_1D = datetime(2017, 1, 1)
end_1D = datetime(2018, 5, 1)

vcb_1D = dhg[(dhg['Date'] > start_1D) & (dhg['Date'] < end_1D)]
vcb_1D.set_index('Date',inplace=True)
vcb_ohlc_1D = vcb_1D['Close'].resample('5D').ohlc()
vcb_volume_1D = vcb_1D['Volume'].resample('5D').sum()

vcb_ohlc_1D.reset_index(inplace=True)
vcb_ohlc_1D['Date']=vcb_ohlc_1D['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan =5, colspan= 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan =1, colspan= 1, sharex = ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, vcb_ohlc_1D.values, width=2, colorup = 'g')
ax2.fill_between(vcb_volume_1D.index.map(mdates.date2num),vcb_volume_1D.values, 0)
plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)
plt.show()

################################STOCK COMBINATION##############################

#Visualizing the Data
#Plot the Price of stock traded each day
fig = plt.figure(figsize = (12, 6))
plt.title('Open')
vcb_nhap['Open'].plot(label = 'VCB')
dhg_nhap['Open'].plot(label = 'DHG')
msn_nhap['Open'].plot(label = 'MSN')
plt.legend()

#Plot the Volume of stock traded each day
fig = plt.figure(figsize = (12, 6))
plt.title('Volume')
vcb_nhap['Volume'].plot(label = 'VCB')
dhg_nhap['Volume'].plot(label = 'DHG')
msn_nhap['Volume'].plot(label = 'MSN')
plt.legend()

#Plot this "Total Traded" against the time index
fig = plt.figure(figsize = (12, 6))
plt.title('Total Traded')
vcb_nhap['Total Traded'].plot(label = 'VCB')
dhg_nhap['Total Traded'].plot(label = 'DHG')
msn_nhap['Total Traded'].plot(label = 'MSN')
plt.legend()

#plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for VCB
fig = plt.figure(figsize = (12, 6))
vcb_nhap.rolling(window = 50).mean()['Open'].plot(label = 'MA50')
vcb_nhap.rolling(window = 200).mean()['Open'].plot(label = 'MA200')
plt.title('VCB')
plt.legend()
#plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for MSN
fig = plt.figure(figsize = (12, 6))
msn_nhap.rolling(window = 50).mean()['Open'].plot(label = 'MA50')
msn_nhap.rolling(window = 200).mean()['Open'].plot(label = 'MA200')
plt.title('MASAN')
plt.legend()
#plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for DHG
fig = plt.figure(figsize = (12, 6))
dhg_nhap.rolling(window = 50).mean()['Open'].plot(label = 'MA50')
dhg_nhap.rolling(window = 200).mean()['Open'].plot(label = 'MA200')
plt.title('DHG')
plt.legend()

#See the relationship between stocks
from pandas.plotting import scatter_matrix
df = pd.concat([vcb_nhap['Open'], dhg_nhap['Open'], msn_nhap['Open']], axis = 1)
df.columns = ['VCB', 'DHG', 'MSN']
df.head()
scatter_matrix(df, figsize = (10, 10), hist_kwds = {'bins' : 100})

###############################EACH STOCK#################################
#huge amount of money traded for each
vcb_nhap['Total Traded'].idxmax()
dhg_nhap['Total Traded'].idxmax()
msn_nhap['Total Traded'].idxmax()
#highest price  for each
vcb_nhap['Close'].idxmax()
dhg_nhap['Close'].idxmax()
msn_nhap['Close'].idxmax()







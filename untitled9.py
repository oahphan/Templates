#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:10:38 2019

@author: MyOanh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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

###candle stick
### Method 1: use matplotlib

from mpl_finance import candlestick_ohlc 
import matplotlib.dates as mdates
vcb_ohlc = vcb_nhap['Close'].resample('10D').ohlc()
vcb_volume = vcb_nhap['Volume'].resample('10D').sum()

vcb_ohlc.reset_index(inplace=True)
vcb_ohlc['Date']=vcb_ohlc['Date'].map(mdates.date2num)
ax1 = plt.subplot2grid((6,1), (0,0), rowspan =5, colspan= 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan =1, colspan= 1, sharex = ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, vcb_ohlc.values, width=2, colorup = 'g')
ax2.fill_between(vcb_volume.index.map(mdates.date2num),vcb_volume.values, 0)
plt.show()
# Save graph to file.
plt.savefig('mpl_vcb.png')

###########################
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
vcb['Date'] = [mdates.date2num(d) for d in vcb['Date']]


####Danh cho visualizing
vcb_index=vcb
dhg_index = dhg
msn_index = msn

#Set index
vcb_index.set_index('Date',inplace=True)
dhg_index.set_index('Date',inplace=True)
msn_index.set_index('Date',inplace=True)

#import library to change the date format
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
vcb['Date'] = [mdates.date2num(d) for d in vcb['Date']]

vcb_candle = vcb.loc[start:end]
#Visualizing the Data
fig = plt.figure(figsize = (12, 6))
plt.title('Open')
vcb_index['Open'].plot(label = 'VCB')
dhg_index['Open'].plot(label = 'dhg')
msn_index['Open'].plot(label = 'MSN')
plt.legend()

#Plot the Volume of stock traded each day
fig = plt.figure(figsize = (12, 6))
plt.title('Volume')
vcb_index['Volume'].plot(label = 'VCB')
dhg_index['Volume'].plot(label = 'DHG')
msn_index['Volume'].plot(label = 'MSN')
plt.legend()

#Create a new column for each dataframe called "Total Traded"
vcb_index['Total Traded'] = vcb['Open'] * vcb['Volume']
dhg_index['Total Traded'] = dhg['Open'] * dhg['Volume']
msn_index['Total Traded'] = msn['Open'] * msn['Volume']

#Plot this "Total Traded" against the time index
fig = plt.figure(figsize = (12, 6))
plt.title('Total Traded')
vcb_index['Total Traded'].plot(label = 'VCB')
dhg_index['Total Traded'].plot(label = 'DHG')
msn_index['Total Traded'].plot(label = 'MSN')
plt.legend()

#huge amount of money traded for VCB 
vcb_index['Total Traded'].argmax()
#plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for VCB
fig = plt.figure(figsize = (12, 6))
vcb_index.rolling(window = 50).mean()['Open'].plot(label = 'MA50')
vcb_index.rolling(window = 200).mean()['Open'].plot(label = 'MA200')
plt.legend()
#plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for MSN
fig = plt.figure(figsize = (12, 6))
msn_index.rolling(window = 50).mean()['Open'].plot(label = 'MA50')
msn_index.rolling(window = 200).mean()['Open'].plot(label = 'MA200')
plt.legend()
#plotting out some MA (Moving Averages). Plot out the MA50 and MA200 for DHG
fig = plt.figure(figsize = (12, 6))
dhg_index.rolling(window = 50).mean()['Open'].plot(label = 'MA50')
dhg_index.rolling(window = 200).mean()['Open'].plot(label = 'MA200')
plt.legend()

#See the relationship between stocks
from pandas.plotting import scatter_matrix
df = pd.concat([vcb_index['Open'], dhg_index['Open'], msn_index['Open']], axis = 1)
df.columns = ['VCB', 'DHG', 'MSN']
df.head()
scatter_matrix(df, figsize = (10, 10), hist_kwds = {'bins' : 100})

# Create the candlestick chart for DHG
DHG_candle = dhg_index.loc[start:end]
DHG_candle = dhg_index.loc[start:end,]
#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from mpl_finance import candlestick_ohlc

# (Year, month, day) tuples suffice as args for quotes_historical_yahoo
mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#import library to change the date format
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
vcb['Index'] = [mdates.date2num(d) for d in vcb['Index']]

#quotes
quotes = [tuple(x) for x in vcb[['Date','Open','High','Low','Close']].values]
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)
#plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, quotes, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()

# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Apple')
 
# Format time.
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
 
plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)
 
# Save graph to file.
plt.savefig('mpl_finance-vcb.png')


fig, ax = plt.subplots()
candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');
 
 
# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Apple')
 
# Format time.
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
 
plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)
 
# Save graph to file.
plt.savefig('mpl_finance-apple.png')






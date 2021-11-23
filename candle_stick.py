#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:28:37 2019

@author: MyOanh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import datetime
from mpl_finance import candlestick_ohlc 
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework
import matplotlib.dates as mdates 
# Avoid FutureWarning: Pandas will require you to explicitly register matplotlib converters.
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#Get data
start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)

vcb_stock = pd.read_csv('./excel_vcb.csv')                     
dhg_stock = pd.read_csv('./excel_dhg.csv')
msn_stock = pd.read_csv('./excel_msn.csv')

#Clean data
vcb = vcb_stock.drop('<Ticker>',axis=1)
dhg = dhg_stock.drop('<Ticker>',axis=1)
msn = msn_stock.drop('<Ticker>',axis=1)
#Rename
vcb = vcb.rename({'<DTYYYYMMDD>':'Date', '<Open>':'Open', '<High>':'High', '<Low>':'Low', '<Close>':'Close', '<Volume>':'Volume'}, axis=1)
dhg = dhg.rename({'<DTYYYYMMDD>':'Date', '<Open>':'Open', '<High>':'High', '<Low>':'Low', '<Close>':'Close', '<Volume>':'Volume'}, axis=1)
msn = msn.rename({'<DTYYYYMMDD>':'Date', '<Open>':'Open', '<High>':'High', '<Low>':'Low', '<Close>':'Close', '<Volume>':'Volume'}, axis=1)
#Format date
vcb['Date'] = vcb['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
dhg['Date'] = dhg['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
msn['Date'] = msn['Date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))

vcb.set_index('Date',inplace=True)
dhg.set_index('Date',inplace=True)
msn.set_index('Date',inplace=True)

# Convert 'Timestamp' to 'float'.
# candlestick_ohlc needs time to be in float days format - see date2num().
vcb['Date'] = [mdates.date2num(d) for d in vcb['Date']]
quotes = [tuple(x) for x in vcb[['Date','Open','High','Low','Close']].values]

# Plot candlestick.
##########################
fig, ax = plt.subplots()
candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');
 
# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('VCB')

# Format time.
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
 
plt.gcf().autofmt_xdate()   # Beautify the x-labels
plt.autoscale(tight=True)
plt.show()
# Save graph to file.
plt.savefig('mpl_finance-VCB.png')
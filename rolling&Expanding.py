#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:30:03 2019

@author: MyOanh
"""
####ROLLING AND EXPANDING
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
# Best way to read in data with time series index!
df = pd.read_csv('time_data/walmart_stock.csv',
                 index_col = 'Date',
                 parse_dates = True)
#Visualising
df['Open'].plot(figsize=(16, 6))
# 7 day rolling mean
df.rolling(7).mean().head(20)
df['Open'].plot()
df.rolling(window = 30).mean()['Close'].plot()
df['Close: 30 Day Mean'] = df['Close'].rolling(window = 30).mean()
df[['Close','Close: 30 Day Mean']].plot(figsize = (16,6))
###Expanding
# Optional specify a minimum number of periods
df['Close'].expanding(min_periods=1).mean().plot(figsize = (16, 6))
##Bollinger Bands
df['Close: 30 Day Mean'] = df['Close'].rolling(window=20).mean()
df['Upper'] = df['Close: 30 Day Mean'] + 2 * df['Close'].rolling(window = 20).std()
df['Lower'] = df['Close: 30 Day Mean'] - 2 * df['Close'].rolling(window = 20).std()
df[['Close','Close: 30 Day Mean','Upper','Lower']].plot(figsize = (16, 6))

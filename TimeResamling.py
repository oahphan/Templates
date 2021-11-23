#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:24:15 2019

@author: MyOanh
"""

###Time Resampling
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Grab data
# Faster alternative
# df = pd.read_csv('time_data/walmart_stock.csv',index_col='Date')
df = pd.read_csv('time_data/walmart_stock.csv')
df.head()
df['Date'] = df['Date'].apply(pd.to_datetime)
df.head()
df.set_index('Date',
             inplace = True)
df.head()
# Our index
df.index
# Yearly Means
df.resample(rule = 'A').mean()
def first_day(entry):
    """
    Returns the first instance of the period, regardless of samplling rate.
    """
    return entry[0]
df.resample(rule = 'A').apply(first_day)
df['Close'].resample('A').mean().plot(kind = 'bar')
plt.title('Yearly Mean Close Price for Walmart')
df['Open'].resample('M').max().plot(kind = 'bar',
                                    figsize = (16, 6))
plt.title('Monthly Max Opening Price for Walmart')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:20:00 2019

@author: MyOanh
"""
#######TIMES SHIFTING
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('time_data/walmart_stock.csv',
                 index_col = 'Date')
df.index = pd.to_datetime(df.index)

df.head()
df.tail()
#.shift() forward
df.shift(1).head()
# You will lose that last piece of data that no longer has an index!
df.shift(1).tail()
#shift() backwards
df.shift(-1).head()
df.shift(-1).tail()

#Shifting based off Time String Cod
# using tshift
## Shift everything forward one month
df.tshift(periods = 1,
          freq = 'M').head()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:13:41 2019

@author: MyOanh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# To illustrate the order of arguments
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15
# January 2nd, 2017
my_date = datetime(my_year,my_month, my_day)
# Defaults to 0:00
my_date 
# January 2nd, 2017 at 13:30:15
my_date_time = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
my_date_time
my_date.day
my_date_time.hour

####Pandas with Datetime Index
# Create an example datetime list/array
first_two = [datetime(2016, 1, 1), datetime(2016, 1, 2)]
first_two
# Converted to an index
dt_ind = pd.DatetimeIndex(first_two)
dt_ind
# Attached to some random data
data = np.random.randn(2, 2)
print(data)
cols = ['A','B']
df = pd.DataFrame(data,dt_ind,cols)
df
df.index
# Latest Date Location
df.index.argmax()
df.index.max()
# Earliest Date Index Location
df.index.argmin()
df.index.min()



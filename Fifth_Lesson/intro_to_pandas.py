#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 07:03:18 2017

@author: ChrisErnst
"""

import pandas as pd
import numpy as np
import os

# Set the directory to
os.chdir('/Users/ChrisErnst/Development/data-science-lessons/Fifth_Lesson')

# Create a datafram
df1 = pd.read_csv("test_data.csv")

# Get the total size of the data frame / matrix
np.shape(df1)

numberRows = np.size(df1, axis=0)
numberCols =np.size(df1, axis=1)

columnNames = df1.columns

column1 = columnNames[0]


first20Rows = df1[0:20]
first20Rows = df1[:20]

first10Rows = df1.head(10)

consump2011 = df1['2011 Average Consumption']

consump2012 = df1['2012 Average Consumption']

consump2013 = df1['2013 Average Consumption']

consump11_13 = df1[['2011 Average Consumption', '2012 Average Consumption', '2013 Average Consumption']]

consump11_13[:20]

dataGraph = df1.plot()

hist = consump2011[:20].plot(kind='bar')

histcounts = consump2013.value_counts()

hist2 = histcounts.plot(kind='bar', ax=None)

histFigure =  hist.get_figure()

histFigure.savefig('test.png')

df1.to_csv('newFileName.csv')


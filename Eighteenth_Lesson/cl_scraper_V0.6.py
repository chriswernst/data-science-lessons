#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:28:42 2017

@author: ChrisErnst
"""

import requests
# For http requests from the internet
from bs4 import BeautifulSoup
# For parsing and creating soup objects
import os
fileSaveDir = os.chdir('/Users/ChrisErnst/Development/data-science-lessons-di/Seventeenth_Lesson')
# Set the directory
from utilities import add_link
from utilities import email_client
# import our link adding function
import numpy as np
# good ol numpy (for matrix and array manipulation)
import pandas as pd
# for exporting to csv
from datetime import datetime
import time


linkList = []
# Create an empty list we will use to hold links

linkList.append(add_link(2001, model='accord')) # 0th element
linkList.append(add_link(2000)) # 1st element
# build our list of urls to specific desired models

page = requests.get(linkList[1])
# Sets page to the target URL

chaos = page.text # requests function
# Makes the html a text-based object
soup = BeautifulSoup(chaos, 'html.parser')
# Uses a html parser to break up the html blocks

newBlockLong = soup.find_all('p', 'result-info')    
# Returns a result set

type(newBlockLong)
len(newBlockLong)

numColumns = 6
ourResultMatrix=[]
for i in range(len(newBlockLong)):
    try:
        ourResultMatrix.append(newBlockLong[i].find('span', 'result-hood').text)
        # First column
        ourResultMatrix.append(newBlockLong[i].find('a', 'result-title hdrlnk').text)
        # Second column
        ourResultMatrix.append(newBlockLong[i].find('span', 'result-price').text)
        # Third Column
        ourResultMatrix.append(newBlockLong[i].find('a', href=True).get('href'))
        # Fourth Column
        ourResultMatrix.append(newBlockLong[i].find('time', href=False).get('datetime'))
        temp = newBlockLong[i].find('time', href=False).get('datetime')
        # Fifth Column
        diff = pd.to_datetime(temp) - pd.Timestamp.today()
        ourResultMatrix.append(diff)
        

    except:
        print("there was an error")
        continue



numRows = len(ourResultMatrix) // numColumns
# Determine the numbe of rows

ourResultMatrix = np.reshape(ourResultMatrix, [numRows, numColumns])
# Reshape into matrix

df = pd.DataFrame(data=ourResultMatrix, columns=['Location', 'Title', 'Price', 'URL', 'Post_Date', 'Posting_Age'])  #.sort_values('Quantity_Sold', ascending=False)
# Create a pandas dataframe

fileName = 'cl_scraper_data' + '.csv'
df.to_csv(fileName, index=False)


email_client(fileName, 'deenrcp@gmail.com')


a = datetime(2011,11,24,0,0,0)
b = datetime(2011,11,17,23,59,59)

a-b
(a-b).days
6


now = pd.Timestamp.today()


postTime = pd.to_datetime('2018-01-22 19:54')

now - postTime


date_time = '01.15.2018 11:05:02'
pattern = '%m.%d.%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
print(epoch)
now =  time.time()


time.time()

datetime.timedelta(datetime.date.today(), )




a = datetime.datetime.now()

b = datetime.datetime.now()

today = datetime.datetime.today()


###### APPENDIX ##################



#for tag in newBlock.find_all(re.compile("^s")):
#    print(tag)
# A helpful way to search by class types
#
#aBlock = soup.find('a', 'result-image gallery')
#
#aBlock = list(aBlock)
#
#
#for sibling in aBlock.next_siblings:
#    aBlock.append(repr(sibling))
#aBlock = aBlock.text
# Run the loop over to fill the list with only prices(print statement optional)
# firstPrice = soup.select_one("span[class*=price]").text
# Returns only one text price    
#links=[]
#for link in soup.find_all('a', href=True):
#    print(link['href'])
#    links.append(link['href'])    
# Creates a list of the links
# List    
# http://www.cademuir.eu/blog/2011/10/20/python-searching-for-a-string-within-a-list-list-comprehension/

# tag = soup.span 
# will only return one item
# aClass = soup.find_all('a') 
# finds all the a class objects
# spanClass = soup.find_all('span')
# finds all the span class objects
# <span class="result-price">$8900</span>

# prices = soup.find_all('span', 'result-price')
# Extract the relevant prices

# prices1 = soup.find('span', 'result-price')

# price1parent = prices1.parent

# newBlock = soup.find('p','result-info')
# This is the line of code!! It pulls the whole 'p' block we are interested in, without all the fluff!
# Returns 'tag' type -  'tag' is a single unit of a 'resultset'

#
#num = 120
## This is page one
## Loop through pages
#for i in range(5):
#    num = num+120
#    URL = ('https://losangeles.craigslist.org/search/sss?query=prius&s=' + str(num) + '&sort=rel' )
#    
#    page = requests.get(URL)
#    # Set the page to the target URL
#    
#    tree = html.fromstring(page.content)
#    # Build html tree
#    
#    soup = BeautifulSoup(page.text, 'html.parser')
#    # Parse with bs4




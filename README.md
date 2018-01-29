# Continuing on Your first program (continued)
##### January 30, 2018
###

### Modules we're using:
1. numpy (to analyze numbers / handle data)
2. os (to set directories)
3. Pandas (to export as csv/analyze data)
4. smptplib (for sending emails)
5. bs4 (for sorting through html)
6. requests (for pulling html pages)


##### Where we left off (V6):
```

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


```

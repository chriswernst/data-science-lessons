# Continuing on Your first program (continued)
##### January 17, 2018
###

### Modules we're using:
1. numpy (to analyze numbers / handle data)
2. os (to set directories)
3. Pandas (to export as csv/analyze data)
4. smptplib (for sending emails)
5. bs4 (for sorting through html)
6. requests (for pulling html pages)


##### Where we left off (V5):
```

import requests
# For going out to the internet
from bs4 import BeautifulSoup
# For parsing and creating soup objects
import os
os.chdir('/Users/ChrisErnst/Development/data-science-lessons/Fifteenth_Lesson')
# Set the directory
from utilities import add_link
# import our link adding function
# This library is for searching
import numpy as np

linkList = []
# Create an empty list we will use to hold links

linkList.append(add_link(2001, model='accord'))
linkList.append(add_link(2000))
# build our list of cars

page = requests.get(linkList[1])
# Sets page to the target URL

chaos = page.text # requests function
# Makes the html a text-based object
soup = BeautifulSoup(chaos, 'html.parser')
# Uses a html parser

newBlockLong = soup.find_all('p', 'result-info')    
# Returns a result set

type(newBlockLong)
len(newBlockLong)

numColumns = 4
ourResultMatrix=[]
for i in range(len(newBlockLong)):
    try:
        ourResultMatrix.append(newBlockLong[i].find('span', 'result-hood').text)
        # One column
        ourResultMatrix.append(newBlockLong[i].find('a', 'result-title hdrlnk').text)
        # Second column
        ourResultMatrix.append(newBlockLong[i].find('span', 'result-price').text)
        # Third Column
        ourResultMatrix.append(newBlockLong[i].find('a', href=True).get('href'))
        # Fourth Column
    except:
        break

numRows = len(ourResultMatrix) // numColumns
# Determine the numbe of rows

ourResultMatrix = np.reshape(ourResultMatrix, [numRows, numColumns])
# Reshape into matrix




```

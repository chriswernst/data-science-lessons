# Finishing Your first program
##### February 15, 2018
###


##### Where we left off (V9):
```


import requests
# For http requests from the internet
from bs4 import BeautifulSoup
# For parsing and creating soup objects
import os
fileSaveDir = '/Users/ChrisErnst/Development/data-science-lessons-di/Twenty_First_Lesson'
os.chdir(fileSaveDir)
# Set the directory
from utilities import add_link
from utilities import email_client
# import our link adding function
import numpy as np
# good ol numpy (for matrix and array manipulation)
import pandas as pd
# for exporting to csv
from time import sleep
inputFileName = 'input_search_list.csv'
inputData = pd.read_csv(inputFileName)
# Read in the input file - Make sure to change this file name and path (above) if you alter the name or location of the input file

delay = 4
# Time delay so our IP doesn't get blocked by Craigslist

print("Searching vehicles from", inputFileName, "\n\n")

print("There are", len(inputData), "unique vehicles in the list\n\n")
estimatedTime = (delay*len(inputData)*5)/60
print("This will take at least", estimatedTime*(1.1), "minutes\n\n  Please be patient")

# Build the linklist with the input data year and model for all counties
linkList = []
# Build an optional linkList for link debugging later on
# import webbrowser as wb # debugging

# Make a request for each of the links, and add it to list ourResultMatrix
ourResultMatrix=[]

for j in range(len(inputData)):
    tempYear = inputData['year'][j]
    tempModel = inputData['model'][j]
    
    print("\nWorking on", tempYear, tempModel , "|    Vehicle " , j+1 , " of" , len(inputData), "\n")
    
    links = add_link(tempYear, model=tempModel)
    
     # for f in range(len(links)):
   
    linkList.append(links)
        
    for x in range(len(links)):
        
        print("\nWorking on link:", x+1, "of",len(links),"\n")
        
        page = requests.get(links[x])
        # Sets page to the target URL
        
        chaos = page.text # requests function
        # Makes the html a text-based object
        soup = BeautifulSoup(chaos, 'html.parser')
        # Uses a html parser to break up the html blocks
        
        newBlockLong = soup.find_all('p', 'result-info')    
        # Returns a result set
        
        print(".........sleeping.........")
        sleep(delay)
            
        numColumns = 8 # For long term use, this should NOT be hardcoded...
        for i in range(len(newBlockLong)):
            try:
                # First column - Neighborhood
                ourResultMatrix.append(newBlockLong[i].find('span', 'result-hood').text) 
                # Second column - Listing Title
                ourResultMatrix.append(newBlockLong[i].find('a', 'result-title hdrlnk').text)
                # Third Column - Car Year
                ourResultMatrix.append(tempYear)
                # Fourth Column - Car Model
                ourResultMatrix.append(tempModel)
                # Fifth Column - Price
                ourResultMatrix.append((newBlockLong[i].find('span', 'result-price').text)[1:])
                # Sixth Column - URL
                ourResultMatrix.append(newBlockLong[i].find('a', href=True).get('href'))
                # Seventh Column - Posting Date and Time
                ourResultMatrix.append(newBlockLong[i].find('time', href=False).get('datetime'))
                
                # Eighth Column - Listing Age (Post date - Current Time)    
                temp = newBlockLong[i].find('time', href=False).get('datetime')
                diff = pd.to_datetime(temp) - pd.Timestamp.today()
                diffInt = int(str(diff)[1:3])
                ourResultMatrix.append(diffInt)
            except:
                continue



numRows = len(ourResultMatrix) // numColumns
# Determine the numbe of rows so we can reshape below

ourResultMatrix = np.reshape(ourResultMatrix, [numRows, numColumns])
# Reshape into matrix

print("\n\n PROCESSING COMPLETE. YOUR MATRIX IS READY.")
print("\nThere are", len(ourResultMatrix), "results")

df = pd.DataFrame(data=ourResultMatrix, columns=['Location', 'Title', 'Year','Model', 'Price', 'URL', 'Post_Date', 'Posting_Age']).apply(pd.to_numeric, errors='ignore').sort_values(['Posting_Age','Price'], ascending=True, kind='mergesort')
# Create a pandas dataframe so we can export to csv

localAveragePrice = round(df['Price'].mean())
# Get the local average price of the result set

stdD = (df['Price'] - localAveragePrice)/localAveragePrice
# Calculate the std dev

df = df.assign(z_score=stdD).sort_values(['Posting_Age','Price', 'z_score'], ascending=True, kind='mergesort')


fileName = 'cl_scraper_data' + '.csv'
df.to_csv(fileName, index=False)

print("\nSaved Successfully to: " + fileSaveDir + "/" + fileName)

email_client(fileName, 'email@gmail.com')



```

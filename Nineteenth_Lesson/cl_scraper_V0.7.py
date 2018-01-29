#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:28:42 2017

@author: ChrisErnst

See utilities.py for useful functions this script uses; as well as appendix.py for unused functions
"""

import requests
# For http requests from the internet
from bs4 import BeautifulSoup
# For parsing and creating soup objects
import os
fileSaveDir = '/Users/ChrisErnst/Development/data-science-lessons-di/Nineteenth_Lesson'
os.chdir(fileSaveDir)
# Set the directory
from utilities import add_link
from utilities import email_client
# import our link adding function
import numpy as np
# good ol numpy (for matrix and array manipulation)
import pandas as pd
# for exporting to csv
import time
inputFileName = 'input_search_list.csv'
inputData = pd.read_csv(inputFileName)
# Read in the input file - Make sure to change this file name and path (above) if you alter the name or location of the input file

linkList = []
# Build an optional linkList for link debugging later on
# import webbrowser as wb # debugging

ourResultMatrix=[]
# Generate an empty list for the links

delay = 5
# Time delay so our IP doesn't get blocked by Craigslist

print("Searching vehicles from", inputFileName, "\n\n")

print("There are", len(inputData), "unique vehicles in the list\n\n")
print("This will take at least", delay*len(inputData), "seconds\n\n  Please be patient")

for j in range(len(inputData)):
    
    print("Working on link:", j+1, "of",len(inputData),"\n")
    tempYear = inputData['year'][j]
    tempModel = inputData['model'][j]
    link = add_link(tempYear, model=tempModel)
    linkList.append(link)
    # Build the linklist with the input data year and model

    page = requests.get(linkList[j])
    # Sets page to the target URL
    
    chaos = page.text # requests function
    # Makes the html a text-based object
    soup = BeautifulSoup(chaos, 'html.parser')
    # Uses a html parser to break up the html blocks
    
    newBlockLong = soup.find_all('p', 'result-info')    
    # Returns a result set
        
    numColumns = 8 # For long term use, this should NOT be hardcoded...
    for i in range(len(newBlockLong)):
        try:
            ourResultMatrix.append(newBlockLong[i].find('span', 'result-hood').text) 
            # First column - Neighborhood
            ourResultMatrix.append(newBlockLong[i].find('a', 'result-title hdrlnk').text)
            # Second column - Listing Title
            ourResultMatrix.append(tempYear)
            # Third Column - Car Year
            ourResultMatrix.append(tempModel)
            # Fourth Column - Car Model
            ourResultMatrix.append(newBlockLong[i].find('span', 'result-price').text)
            # Fifth Column - Price
            ourResultMatrix.append(newBlockLong[i].find('a', href=True).get('href'))
            # Sixth Column - URL
            ourResultMatrix.append(newBlockLong[i].find('time', href=False).get('datetime'))
            # Seventh Column - Posting Date and Time
            temp = newBlockLong[i].find('time', href=False).get('datetime')
            diff = pd.to_datetime(temp) - pd.Timestamp.today()
            ourResultMatrix.append(diff)
            # Eighth Column - Listing Age (Post date - Current Time)    
        except:
            continue
    print(".........sleeping.........")
    time.sleep(delay)
    

numRows = len(ourResultMatrix) // numColumns
# Determine the numbe of rows so we can reshape below

ourResultMatrix = np.reshape(ourResultMatrix, [numRows, numColumns])
# Reshape into matrix

print("\n\n PROCESSING COMPLETE. YOUR MATRIX IS READY.")
print("\nThere are", len(ourResultMatrix), "results")

df = pd.DataFrame(data=ourResultMatrix, columns=['Location', 'Title', 'Year','Model', 'Price', 'URL', 'Post_Date', 'Posting_Age']) #.sort_values('Posting_Age', ascending=False)
# Create a pandas dataframe so we can export to csv

fileName = 'cl_scraper_data' + '.csv'
df.to_csv(fileName, index=False)

print("\nSaved Successfully to: " + fileSaveDir + "/" + fileName)

email_client(fileName, 'deenrcp@gmail.com')


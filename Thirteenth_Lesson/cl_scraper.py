#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:28:42 2017

@author: ChrisErnst
"""

import requests
# For going out to the internet
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer
import webbrowser as wb
import os

# Import all the libraries

prius2015 = 'https://losangeles.craigslist.org/search/wst/sss?query=prius+-salvage&sort=rel&min_price=999&max_price=15000&min_auto_year=2015&max_auto_year=2015&min_auto_miles=10000&max_auto_miles=100000'

civic2000 = 'https://losangeles.craigslist.org/search/cto?query=%282000+civ*%29+-salv*&srchType=T&bundleDuplicates=1&searchNearby=2&nearbyArea=104&nearbyArea=103&nearbyArea=209&nearbyArea=208&min_price=999&max_price=15000&min_auto_miles=999&max_auto_miles=110000'
# URL link to CL

page = requests.get(civic2000)
# Sets page to the target URL

chaos = page.text # requests function
# Makes the html a text-based object
soup = BeautifulSoup(chaos, 'html.parser')
# Uses a html parser

tag = soup.span 
# will only return one item
aClass = soup.find_all('a') 
# finds all the a class objects
spanClass = soup.find_all('span')
# finds all the span class objects
# <span class="result-price">$8900</span>

prices = soup.find_all('span', 'result-price')
# Extract the relevant prices

priceList = []
# Create an empty list
for i in prices:
    priceList.append(i.text)
    print(i.text)
# Run the loop over to fill the list with only prices(print statement optional)
# firstPrice = soup.select_one("span[class*=price]").text
# Returns only one text price
    
    
titles = soup.find_all('a', 'result-title hdrlnk')
titleList = []
# Create an empty list
for i in titles:
    titleList.append(i.text)
    print(i.text)
    
    
    
links=[]
for link in soup.find_all('a', href=True):
    print(link['href'])
    links.append(link['href'])    
# Creates a list of the links
# List    
# http://www.cademuir.eu/blog/2011/10/20/python-searching-for-a-string-within-a-list-list-comprehension/

for link in BeautifulSoup(chaos, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])




for i in soup.find_all('a', 'result-price'):
    print(i['class'])
















condition_groups = soup.find_all('p',{'class': 'attrgroup'})
# car conditions






links=[]
for link in soup.find_all('a', href=True):
    print(link['href'])
    links.append(link['href'])
# Parses all the links

soup.select('a[href]')
soup.select('span')

soup.get_text()

tree = html.fromstring(page.content)
# Build html tree

soup = BeautifulSoup(page.text, 'html.parser')
# Parse with bs4

URL = ('https://losangeles.craigslist.org/search/sss?query=prius&s=' + str(num) + '&sort=rel' )

num = 120
# This is page one
# Loop through pages
for i in range(5):
    num = num+120
    URL = ('https://losangeles.craigslist.org/search/sss?query=prius&s=' + str(num) + '&sort=rel' )
    
    page = requests.get(URL)
    # Set the page to the target URL
    
    tree = html.fromstring(page.content)
    # Build html tree
    
    soup = BeautifulSoup(page.text, 'html.parser')
    # Parse with bs4




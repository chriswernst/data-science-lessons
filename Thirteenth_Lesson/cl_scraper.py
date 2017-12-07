#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:28:42 2017

@author: ChrisErnst
"""

import requests
# For going out to the internet
from lxml import html
from bs4 import BeautifulSoup
import webbrowser as wb
import os

# Import all the libraries

prius2015 = 'https://losangeles.craigslist.org/search/wst/sss?query=prius+-salvage&sort=rel&min_price=999&max_price=15000&min_auto_year=2015&max_auto_year=2015&min_auto_miles=10000&max_auto_miles=100000'

page = requests.get(prius2015)
# Set the page to the target URL
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
soup.find_all("span", "title")

prices = soup.find_all('span', 'result-price')

links = soup.find_all('span', 'result-price')

divClass = soup.find_all('div')






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








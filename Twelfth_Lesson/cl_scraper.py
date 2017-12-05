#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:28:42 2017

@author: ChrisErnst
"""

import requests
import bs4
from lxml import html
from bs4 import BeautifulSoup
import webbrowser as wb

# Import all the libraries

page = requests.get('https://losangeles.craigslist.org/search/sss?query=prius&sort=rel')
# Set the page to the target URL

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








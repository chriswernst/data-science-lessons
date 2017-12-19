#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:28:42 2017

@author: ChrisErnst
"""

import requests
# For going out to the internet
from lxml import html
# For parsing
from bs4 import BeautifulSoup, SoupStrainer
import os
os.chdir('/Users/ChrisErnst/Development/data-science-lessons/Fourteenth_Lesson')
# Set the directory
from utilities import add_link
# import our link adding function
import re
# This library is for searching

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

tag = soup.span 
# will only return one item
aClass = soup.find_all('a') 
# finds all the a class objects
spanClass = soup.find_all('span')
# finds all the span class objects
# <span class="result-price">$8900</span>

prices = soup.find_all('span', 'result-price')
# Extract the relevant prices

prices1 = soup.find('span', 'result-price')

price1parent = prices1.parent




newBlock = soup.find('p','result-info' )
# This is the line of code!! It pulls the whole 'p' block we are interested in, without all the fluff!

newBlock = list(newBlock)


price = newBlock.find_all('span','result-price')

hood = newBlock.find_all('span', 'result-hood')


ourList = []
# Create an empty list
for i in price:
    ourList.append(i.text)
    print('adding', i.text, 'to the list')
    
for i in hood:
    ourList.append(i.text)
    print('adding', i.text, 'to the list')
# These loops remove the junk    

print(ourList)



for tag in newBlock.find_all(re.compile("^s")):
    print(tag)
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







priceList = []
# Create an empty list
for i in prices:
    priceList.append(i.text)
    print(i.text)
# Run the loop over to fill the list with only prices(print statement optional)
# firstPrice = soup.select_one("span[class*=price]").text
# Returns only one text price
    
# There are duplicate prices; Remove redundant Records:
type(priceList)
setPriceList = set(priceList)
# Instead of this we may want to specifically select the records
priceList = list(setPriceList)





    
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




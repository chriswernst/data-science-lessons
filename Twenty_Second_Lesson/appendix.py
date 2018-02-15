#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:40:21 2018

@author: ChrisErnst

The following are unused functions to support the cl_scraper_VX.X.py
"""



###### APPENDIX ##################



#
#now = pd.Timestamp.today()
#
#postTime = pd.to_datetime('2018-01-22 19:54')
#
#now - postTime
#
#date_time = '01.15.2018 11:05:02'
#pattern = '%m.%d.%Y %H:%M:%S'
#epoch = int(time.mktime(time.strptime(date_time, pattern)))
#print(epoch)
#now =  time.time()
#
#time.time()
#
#datetime.timedelta(datetime.date.today(), )
#
#a = datetime.datetime.now()
#
#b = datetime.datetime.now()
#
#today = datetime.datetime.today()
#
#a = datetime(2011,11,24,0,0,0)
#b = datetime(2011,11,17,23,59,59)
#
#a-b
#(a-b).days
#
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

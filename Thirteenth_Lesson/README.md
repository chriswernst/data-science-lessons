# Putting it all together - Your first program (continued)
##### December 7, 2017
###### by Chris Ernst
###

### Modules we may use(not exhaustive):
1. numpy (to analyze numbers / handle data)
2. os (to set directories)
3. Pandas (to export as csv/analyze data)
4. lxml (for parsing html)
5. csv (to export as csv)
6. smptplib (for sending emails)
7. bs4 (for sorting through html)
8. requests (for pulling html pages)


##### Where we left off:
```
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


```

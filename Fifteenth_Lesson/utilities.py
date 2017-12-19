#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:31:38 2017

@author: ChrisErnst
"""


# create a link adder function:
def add_link(year, model='civic'):
    try:
        model = str(model)
        year =  str(year)
        # Convert to strings
        link = ('https://losangeles.craigslist.org/search/cto?query=%28' + year + '+' + model + '*%29+-salv*&srchType=T&bundleDuplicates=1&searchNearby=2&nearbyArea=104&nearbyArea=103&nearbyArea=209&nearbyArea=208&min_price=999&max_price=15000&min_auto_miles=999&max_auto_miles=110000')
        # Build the link as a string        
        return link
    except:
        print ("please make sure to use quotes around car model")
    
    


        

    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:14:13 2018

@author: ChrisErnst
"""


########################## JSON DATA - SIMILAR TO PYTHON DICTIONARY ##########

APIKey = {
        'model':'tacoma',
        "year":"2001",
        "make":"toyota",
        "engine": "4 cylinder",
        "mpg":"20/28",
        "transmission":"manual",
        "mileage":"142000",
        "color":"grey",
        "price":"7000",
        "zip":"94530",
        }



########################### XML DATA - SIMILAR TO HTML ##############################

import os
os.chdir('/Users/ChrisErnst/Development/data-science-lessons-di/Twenty_Fourth_Lesson')

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

root.tag

for child in root:
    print (child.tag, child.attrib)
    

root[0][1].text


country_data_as_string = '<?xml version="1.0"?> \
                            <data>
                                <country name="Liechtenstein">
                                    <rank>1</rank>
                                    <year>2008</year>
                                    <gdppc>141100</gdppc>
                                    <neighbor name="Austria" direction="E"/>
                                    <neighbor name="Switzerland" direction="W"/>
                                </country>
                                <country name="Singapore">
                                    <rank>4</rank>
                                    <year>2011</year>
                                    <gdppc>59900</gdppc>
                                    <neighbor name="Malaysia" direction="N"/>
                                </country>
                                <country name="Panama">
                                    <rank>68</rank>
                                    <year>2011</year>
                                    <gdppc>13600</gdppc>
                                    <neighbor name="Costa Rica" direction="W"/>
                                    <neighbor name="Colombia" direction="E"/>
                                </country>
                            </data>'

root = ET.fromstring(country_data_as_string)


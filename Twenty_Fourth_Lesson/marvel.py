#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:46:01 2018

@author: ChrisErnst


"""
import time
import hashlib
import requests
import webbrowser as wb
publicKey =''
privateKey = ''

m = hashlib.md5()

ts = str(round(time.time()))

ourHash = ts + privateKey + publicKey

m.update(ourHash.encode('utf-8'))
m.digest()

link = 'http://developer.marvel.com/v1/public/comics?ts=' + ts + '&apikey=' + publicKey + '&hash=' + ourHash

r = requests.get(link)
r.text
wb.open(link)
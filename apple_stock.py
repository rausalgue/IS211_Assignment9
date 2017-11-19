#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Nine - Fetch Apple Stock Data"""

"""
output the close price and date for all the dates shown on the page
"""

import urllib2
from bs4 import BeautifulSoup

data_url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
page = urllib2.urlopen(data_url)
soup = BeautifulSoup(page.read(),'html.parser')

print 'Fetching Stock Data'
#print soup.prettify()

print 'Processing Data...'

trs = soup.find_all('tr')
for tr in trs:
    tds = tr.find_all("td")

    try:  # we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        date = str(tds[0].get_text())  # This structure isolate the item by its column in the table and converts it into a string.
        close_price = str(tds[4].get_text())

    except:
        #print "bad tr string"
        continue  # This tells the computer to move on to the next item after it encounters an error

    print 'Stock Information:',date,'Closed At:',close_price
    #print tds
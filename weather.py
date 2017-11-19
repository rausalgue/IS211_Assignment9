#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Nine - Weather data"""

"""
1. Display the actual temperatures for the days of the month that have passed
2. Display the forecasted temperatures for the days of the month that have not passed yet
"""

import urllib2
from bs4 import BeautifulSoup

data_url = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
page = urllib2.urlopen(data_url)
soup = BeautifulSoup(page.read(),'html.parser')

print 'Fetching Weather Data'
#print soup.prettify()

print 'Processing Data...'

trs = soup.find_all('tr')
for tr in trs:
    tds = tr.find_all("td")
    span = tr.find_all('span')

    try:  # we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        date = str(tds[0].get_text())  # This structure isolate the item by its column in the table and converts it into a string.
        high = int(span[0].get_text())
        avg = int(span[1].get_text())
        low = int(span[2].get_text())

    except:
        #print "bad tr string"
        continue  # This tells the computer to move on to the next item after it encounters an error

    print 'Weather Information: Date',date,'High:',high,'Average:',avg,'Low:',low
    #print tds
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Nine - Fetch Football Stats"""

"""
output the list of top 20 players, including the player’s position, team and total number of
touchdowns
"""

import urllib2
from bs4 import BeautifulSoup

data_url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns'
page = urllib2.urlopen(data_url)
soup = BeautifulSoup(page.read(),'html.parser')

print 'Fetching Football Data'
#print soup.prettify()

print 'Processing Data...'

counter = 0

trs = soup.find_all('tr')
for tr in trs:
    tds = tr.find_all("td")

    #print counter


    try:  # we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text())  # This structure isolate the item by its column in the table and converts it into a string.
        position = str(tds[1].get_text())
        team = str(tds[2].get_text())
        tot_td = str(tds[6].get_text())

        counter +=1

        if counter == 21:
            break

    except:
        #print "bad tr string"
        continue  # This tells the computer to move on to the next item after it encounters an error

    print 'Player Iteration:',counter,'--',names, position, team, tot_td




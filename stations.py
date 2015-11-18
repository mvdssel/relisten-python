#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib2

homePage = 'https://relisten.be'
stationIdentifierRegexp = re.compile('data-stationurl="([^"]+)"')

def getStations():
    response = urllib2.urlopen(homePage)
    html = response.read()
    return re.findall(stationIdentifierRegexp, html)

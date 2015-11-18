#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import csv
from playlists import getPlaylists

# Settings
filename = 'playlists.csv'
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)

# Get all the songs
playlists = getPlaylists(yesterday, today)

# Get a file writer
csvFile = open(filename, 'wb')
csvWriter = csv.DictWriter(
    csvFile,
    fieldnames=playlists[0].keys(),
    delimiter=';',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL
)

# Write all songs to the csv
for song in playlists:
    csvWriter.writerow(song)

print 'Wrote results to ' + filename

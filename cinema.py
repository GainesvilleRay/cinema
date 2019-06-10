"""Code to format info on movies in a csv file for publication.

This is a hot mess.

"""

# libraries
#from collections import defaultdict
import csv
import datetime
from datetime import date
import glob
#from itertools import chain
import os.path, time
import numpy as np
import pandas as pd
import shutil
from tempfile import NamedTemporaryFile

# Find newest csv file in the directory and use it.
directory = '/Users/Doug/workspace/cinema/*.csv'
list_of_files = glob.glob(directory)
latest_file = max(list_of_files, key=os.path.getctime)
newfile = latest_file.split('cinema/')[-1]

# Edit problems in the newfile
with open(newfile) as csv_file:
    reader = csv.reader(csv_file, delimiter= ',', quotechar='"')

    for row in reader:
        row[0] = row[0].split(', FL')[0]
        row[5] = row[5].replace('p | ', ' p.m., ')
        row[5] = row[5].replace('a | ', ' a.m., ')
        row[5] = row[5].replace('0p', '0 p.m.')
        row[5] = row[5].replace('5p', '5 p.m.')
        row[5] = row[5].replace(':00', '')
        row[5] = row[5].replace(' p.m.,', ',')

ocala_market = ['Ocala, FL', 'Belleview, FL', 'The Villages, FL']
gnv_market = ['Gainesville FL', 'High Springs, FL', 'Starke, FL']

amc_lake = 'AmC Lake Square 12'
barnstorm = 'Barnstorm Theater'
celebration10 = 'Celebration Point 10'
fla_twin = 'Florida Twin'
hipp = 'Hippodrome State Theatre'
marion_th = 'Marion Theatre'
ocala6 = 'Ocala Center 6'
old_mill = 'Old Mill Playhouse'
butler = 'Regal Butler Town Center 14'
imax_ocala = 'Regal Hollywood Stadium 16 & IMAX - Ocala'
regal_royal = 'Regal Royal Park Stadium 16'
reitz = 'Reitz Union Cinema - U of Fl'
rialto = 'Rialto Theatre Spanish Springs Town Square'

def ocaladaily_pn():
    """ Build print narrative for Ocala daily editions """
    with open(newfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if row[9] in gnv_market:
                movie_stuff = f"\"{row[2]}\", {row[3]}, {row[4]}, {row[6]}, {row[7]}"
                theater_stuff = f'{row[1]}, {row[0]}, {row[5]}'
                listing = movie_stuff + theater_stuff
                listings.append(listing)
    return listings

scene_pn()

def go_pn():
    """ Build print narrative for Go! section in Gainesville """
    listing = []
    listings = []
    f=open('golistings.txt', 'a')
    f.write('MOVIE TIMES' + '\n\n')
    ocala_market = ['Ocala, FL', 'Belleview, FL', 'The Villages, FL']
    gnv_market = ['Gainesville FL', 'High Springs, FL', 'Starke, FL']
    belleview = 'Belleview, FL'
    hipp = 'Hippodrome State Theatre'
    ocala = 'Ocala, FL'

    with open('2781_Fandango_data_Movie_full.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if row[9] in ocala_market:
                row[0] = row[0].split(', FL')[0]
                row[5] = row[5].replace('p | ', ' p.m., ')
                row[5] = row[5].replace('a | ', ' a.m., ')
                row[5] = row[5].replace('0p', '0 p.m.')
                row[5] = row[5].replace('5p', '5 p.m.')
                row[5] = row[5].replace(':00', '')
                movie_stuff = f"\"{row[2]}\", {row[3]}, {row[4]}, {row[6]}, {row[7]}"
                theater_stuff = f'{row[1]}, {row[0]}, {row[5]}'
                listing = movie_stuff + theater_stuff
                listings.append(listing)

                f.write(movie_stuff + )
    return listings

go_pn()

def gnvdaily_pn():
    """ Builds print narrative for Gainesville daily editions """
    listing = []
    listings = []
    ocala_market = ['Ocala, FL', 'Belleview, FL', 'The Villages, FL']
    gnv_market = ['Gainesville FL', 'High Springs, FL', 'Starke, FL']
    with open('2781_Fandango_data_Movie_full.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            if row[9] in ocala_market:
                row[0] = row[0].split(', FL')[0]
                row[5] = row[5].replace('p | ', ' p.m., ')
                row[5] = row[5].replace('a | ', ' a.m., ')
                row[5] = row[5].replace('0p', '0 p.m.')
                row[5] = row[5].replace('5p', '5 p.m.')
                row[5] = row[5].replace(':00', '')
                movie_stuff = f"\"{row[2]}\", {row[3]}, {row[4]}, {row[6]}"
                theater_stuff = f'{row[1]}, {row[0]}, {row[5]}'
                listing = movie_stuff + theater_stuff
                listings.append(listing)
    return listings

gnvdaily_pn()

""" ___________________ """

# Odds and ends

# Creates list of dictionaries for each row, assigns field name for key in all pairs. This is working.
listings = []
scrape_file = '2781_Fandango_data_Movie_full.csv'
with open(scrape_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        layout_dct = {'addy': row[0], 'theater': row[1], 'title': row[2], 'mpaa': row[3], 'stars': row[4], 'times': row[5], 'format': row[6], 'synopsis': row[7], 'date': row[8], 'city': row[9]}
        listings.append(layout_dct)

del listings[0] #remove header row

print(listings)

""" ______________________ """

# Finds next dictionary in list where a key is matched with a particular value
next(item for item in listings if item['stars'] == '4.5')

# Function to find a dictionary listing with a particular key:value; similar to above
def search(list, key, value):
    for item in list:
        if item[key] == value:
            return item

search(listings, 'mpaa', 'R')

# Effort to join showtimes if theater == one above. Not working
listings = []
scrape_file = '2781_Fandango_data_Movie_full.csv'
with open(scrape_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        layout_dct = {'addy': row[0], 'theater': row[1], 'title': row[2], 'mpaa': row[3], 'stars': row[4], 'times': row[5], 'format': row[6], 'synopsis': row[7], 'date': row[8], 'city': row[9]}
        if row[1] == row[1]:
            for 'times', row[5] in listings:
                listings.append('times', row[5])
        listings.append(layout_dct)

del listings[0] #remove header row

""" __________________________ """


# This uses defaultdict to join items in a tuple as a list
s = [('regal', (1, 2)), ('amc', (3, 5)), ('regal', (2, 4)), ('amc', (7, 9))]
d = defaultdict(list)
for k, v in s:
    if k == k:
        d[k].append(v)

sorted(d.items())


""" __________________________ """

# structure and format for Friday listings
# create a class for Friday movie
class Movie:

    def __init__(self, title, stars, mpaa, runtime, genre, about):
        self.title = title
        self.stars = stars
        self.mpaa = mpaa
        self.runtime = runtime
        self.genre = genre
        self.about = about

    def LifeTag(self):
        return self.title + " (" + self.mpaa + ") "

    def SceneTag(self):
        return "\"\"" + self.title + "\"\"\n" + self.stars + "\n" + self.mpaa + ": " + self.about

class Screening(Movie):

    def __init__(self, title, cinema, showdate, showtime):
        Movie.__init__(self, title)
        Movie.__init__(self, mpaa)
        self.cinema = cinema
        self.showdate1 = showdate
        self.showtime = showtime

Creed = Movie("Creed II", "3 1/2", "PG-13", "180 minutes", "Sports", "This sequel ...")
Ralph = Movie("Ralph Breaks the Internet", "", "PG", "60 minutes", "Animation", "Six years after ...")

# One approach might be to create a class for a listing
# that has subclasses for movies and theaters

class Listing:

    '''Class for a movie listing that outputs the fully
    formatted listing for publication.'''

    def __init__(self):
        self.what = 'what should go here?'

    class Movie:
        def __init__(self, title, stars, mpaa, runtime, genre, about):
            self.title = title
            self.stars = stars
            self.mpaa = mpaa
            self.runtime = runtime
            self.genre = genre
            self.about = about
                return 'narrative common to'

class Cinema:

    '''Class for area movie theatre'''

    def __init__(self, theater, addy, market, showtimes):
        self.theater = theater
        self.addy = addy
        self.market = market
        self.showtimes = showtimes

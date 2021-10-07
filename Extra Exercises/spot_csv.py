"""
Spotify CSV artists

Use the csv.reader() method to read the top-spotify-songs.csv which contains a list of top songs from the last 10 years.

After that create an artists list containing all the artist names from the file.

Finally, use the Counter method to count how many times appears each artist and store the top 5 artists 
"""

import csv
from collections import Counter

artists = []
top_artists = []

import csv
from collections import Counter

with open('top-spotify-songs.csv', 'r') as file:
    reader = csv.reader(file)
    artists = []

    for row in reader:
        if row[0] != '0':
            artists.append(row[2])
            

top_artists = Counter(artists).most_common()[:5]
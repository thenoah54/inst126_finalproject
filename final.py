from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os
# 3.17/3.18
import classification

# custome error message 
class CustomError(Exception):
    "Custom Error"
    pass 

set_date = classification.set_date()

if len(set_date) != 10:
    raise CustomError("Invalid Date")

# test
# response = requests.get("https://www.billboard.com/charts/hot-100/2023-11-25/")
# 10.1
response = requests.get(f"https://www.billboard.com/charts/hot-100/{set_date}/")
webpage = response.text
# 10.2
soup = BeautifulSoup(webpage, "html.parser")

# 10.3
# finds the title using CSS selectors. h3 in a li in a ul in a li tag
title_tags = soup.select(selector="li ul li h3")
# because the number one song's class is different for some reason
number_one_artist = soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
artist_tags = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

# print(title_tags)
# print(len(title_tags))
# 5.7
songs = []
artists = []
for title in title_tags:
    # 5.9
    songs.append(title.getText().strip())
# 5.8
artists.append(number_one_artist.getText().strip())
for artist in artist_tags:
    artists.append(artist.getText().strip())

try:
    with open("songs.txt", 'r') as file:
        None
except FileNotFoundError:
    print("Creating new file...")
    # 3.20
    with open("songs.txt", 'w') as file:
        None

# song_artist = []
# for i in range(len(songs)):
#     song_artist.append(classification.artist_song_tuple(songs, artists))

# 5.15
songs_100 = {}
counter = 1
date = True
if os.path.exists("songs.txt") == True:
    try:
        for i in range(0, 100):
            # 5.17/5.18/5.19/5.13
            songs_100[counter] = classification.artist_song_tuple(songs, artists)[0][i]
            # writes the date once
            while date:
                with open("songs.txt", 'a') as file:
                    file.write(f"###### {set_date} ######\n")
                    date = False
            with open("songs.txt", 'a') as file:
                # 3.21
                file.write(f"{counter}: {classification.artist_song_tuple(songs, artists)[0][i]} by, {classification.artist_song_tuple(songs, artists)[1][i]}\n")
            counter += 1
        # print(set_date)
        # pprint(songs_100) 
    except IndexError:
        # 4.9
        CustomError("Invalid Date")

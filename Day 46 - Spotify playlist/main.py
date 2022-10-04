from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


CHART_URL="https://www.billboard.com/charts/hot-100/"
SPOTIFY_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

def add_to_list(name, mode):
    with open ("C:\PyLearning\projects\Day 46 - Spotify playlist\list.txt", mode) as file:
        file.write(f"{name}\n")

#Search billboard for specified date and create list of songs
date = input("What date would you like to go to (YYYY-MM-DD): ")
response = requests.get(f"{CHART_URL}{date}")
scraping = BeautifulSoup(response.text, "html.parser")
song_titles = []
main_headline = scraping.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
main_song = (main_headline[0].getText()).strip()
add_to_list(main_song, "w")

headlines = scraping.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
for headline_tag in headlines:
    title = (headline_tag.getText()).strip()
    add_to_list(title, "a")


#Spotify Auth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
        )
    )
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
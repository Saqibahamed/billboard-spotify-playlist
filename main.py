import spotipy
from spotipy.oauth2 import SpotifyOAuth
import Billboard_Scraping
import requests
import pprint
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".venv/.env")

# connecting to spotify API

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URL = os.environ['REDIRECT_URL']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               scope="playlist-modify-public",
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username='Saqib Sharief'))

# getting user ID
user_id = sp.current_user()["id"]

# getting songs from billboard scraping

songs = Billboard_Scraping.get_songs()

# extracting year from the input date
year = Billboard_Scraping.date.split('-')[0]

# creating a list of URI for all the songs from billboard

song_uri = []

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uri.append(result['tracks']['items'][0]['uri'])
        print('song added...')

    except IndexError:
        print("does not exist in spotify....skipped")

# creating a playlist:

create_playlist = sp.user_playlist_create(user=user_id,
                                          name=f'Top 100 songs - {year}',
                                          public=True)
# adding songs to playlist:

add_tracks_playlist = sp.playlist_add_items(playlist_id=create_playlist['id'],
                                            items=song_uri)
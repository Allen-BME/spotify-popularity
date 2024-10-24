import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np


def get_album_id(sp,album,artist):
    return sp.search(q=f"album:{album} artist:{artist}", type="album", limit=1)["albums"]["items"][0]["id"]

def get_album_popularity_array(album_id):
    tracks = sp.album_tracks(album_id)['items']
    return np.array([
        [sp.track(track['id'])['popularity'], sp.track(track['id'])['duration_ms']]
        for track in tracks])


# client details from environment vars
client_id = os.environ["SPOTIFY_ID"]
client_secret = os.environ["SPOTIFY_SECRET"]

# open spotify session
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

album_id = get_album_id(sp, "Collide With the Sky", "Pierce the Veil")
popularity_arr = get_album_popularity_array(album_id)

print(popularity_arr)

print("ran main.py!")
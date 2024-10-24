import time
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np

t1 = time.time()

def get_album_id(album,artist):
    return sp.search(q=f"album:{album} artist:{artist}", type="album", limit=1)["albums"]["items"][0]["id"]

def get_albums_id(albums):
    return [
        sp.search(q=f"album:{album} artist:{artist}", type="album", limit=1)["albums"]["items"][0]["id"] for (album,artist) in albums
    ]

def get_album_popularity_array(album_id):
    tracks = sp.album_tracks(album_id)['items']
    return np.array([
        [sp.track(track['id'])['popularity'], sp.track(track['id'])['duration_ms']]
        for track in tracks])

def get_albums_popularity_array(album_ids):
    albums_popularities = dict()
    for album_id in album_ids:
        tracks = sp.album_tracks(album_id)['items']
        albums_popularities[album_id] = np.array([
            [sp.track(track['id'])['popularity'], sp.track(track['id'])['duration_ms']]
            for track in tracks])
    return albums_popularities

# client details from environment vars
client_id = os.environ["SPOTIFY_ID"]
client_secret = os.environ["SPOTIFY_SECRET"]

# open spotify session
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# list of albums to collect data for
albums = [
    ("Collide With the Sky", "Pierce the Veil"),
    ("Something to Write Home About", "The Get Up Kids"),
    ("Songs In The Key Of Life", "Stevie Wonder"),
    ("Past Lives", "L.S. Dunes"),
    ]

album_ids = get_albums_id(albums)
albums_popularities = get_albums_popularity_array(album_ids)
print(albums_popularities)

print(f"ran main.py in: {(time.time()-t1):.2f} s")
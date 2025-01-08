import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
load_dotenv(dotenv_path="../.env")
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
scope = "user-top-read"
authorizer = SpotifyOAuth( client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
music = spotipy.Spotify(auth_manager=authorizer)
top_tracks = music.current_user_top_tracks(limit=20, offset=0, time_range='long_term')
counter = 1
for track in top_tracks['items']:
    track_name = track['name']
    artists = ", ".join([artist['name'] for artist in track['artists']])
    print(f"{counter}. {track_name} by {artists}")
    counter = counter + 1


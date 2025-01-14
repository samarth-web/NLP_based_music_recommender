import streamlit as st
import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
import time
import cv2
from deepface import DeepFace
def emotion_detection():
   
    cam = cv2.VideoCapture(0)
    ret,frame = cam.read()
    print(ret)

            
    enforce_detection=False    
            

    cam.release()
    if ret == False:
        print("No camera detected")
    else:
        print("Camera detected")
        analysis = DeepFace.analyze(frame, actions=['race', 'emotion', 'age', 'gender'])
        if isinstance(analysis, list):

            print("analysis is a list")
        else:

            print("analysis is not a list")
            print(analysis)
            print(len(analysis))
            trial = analysis[0]
            print("Race analysis:", trial.get("dominant_race"))
            print("Emotion:", trial.get("dominant_emotion"))
            print("Age:", trial.get("age"))
            print("Gender:", trial.get("dominant_gender"))
            # print("Age:", analysis.get("age"))
            # print("Gender:", analysis.get("gender"))
            return trial.get("dominant_emotion")

def music_creation():
    load_dotenv(dotenv_path="../.env")
    CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
    scope = "user-top-read playlist-modify-public"
    authorizer = SpotifyOAuth( client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
    music = spotipy.Spotify(auth_manager=authorizer)
    time_pref = 'long_term'
    top_tracks = music.current_user_top_tracks(limit=50, offset=0, time_range=time_pref)
    song_links = []
    counter = 1

    var = 0
    for track in top_tracks['items']:
        track_name = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        print(f"{counter}. {track_name} by {artists}")
        song_links.append(track['uri'])
        counter = counter + 1
    print("Public playlist created in Spotify account")
    user_id = music.current_user()['id']
    playlist_name = "My Top 50 Tracks"
    playlist_description = f"A playlist of my {time_pref} top 50 tracks via Spotify API"
    playlist_created = music.user_playlist_create( user=user_id,  name=playlist_name,  public=True,  description=playlist_description )
    time.sleep(2)
    music.playlist_add_items(playlist_id=playlist_created['id'], items=song_links)
    print("Check your spotify app now : ")
    playlist_id = playlist_created['id']
    embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"

    st.title('Mood Music Recommendation')
    st.markdown(
        f"""
        <iframe src="{embed_url}" 
        width="400" 
        height="600" 
        frameborder="0" 
        allowtransparency="true" 
        allow="encrypted-media"></iframe> 
        """,
        unsafe_allow_html=True #tested
    )
     img_data = st.camera_input("Take a photo")
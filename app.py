import streamlit as st
import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
import time
import cv2
from deepface import DeepFace
import pandas as pd
import numpy as np
import time
def emotion_detection():
   
    cam = cv2.VideoCapture(0)
    ret,frame = cam.read()
    print(ret)

            
      
            

    cam.release()
    if ret == False:
        print("No camera detected")
    else:
        enforce_detection=False  
        print("Camera detected")
        analysis = DeepFace.analyze(frame, actions=['emotion'],enforce_detection=False)
        
        print("analysis is a list")
        

            # print("analysis is not a list")
            # print(analysis)
            # print(len(analysis))
        trial = analysis[0]
            # print("Race analysis:", trial.get("dominant_race"))
            # print("Emotion:", trial.get("dominant_emotion"))
            # print("Age:", trial.get("age"))
            # print("Gender:", trial.get("dominant_gender"))
            # print("Age:", analysis.get("age"))
            # print("Gender:", analysis.get("gender")
        print(trial.get("dominant_emotion"))
        return trial.get("dominant_emotion")

def get_spotify_track_ids(music, song_titles, artist_names):
   
    spotify_ids = []
    
    for song, artist in zip(song_titles, artist_names):
        query = f"track:{song} artist:{artist}"
        results = music.search(q=query, type="track", limit=1)

        if results['tracks']['items']:
            spotify_ids.append(results['tracks']['items'][0]['id'])  # Get the first match
        else:
            print(f"Track not found: {song} by {artist}")
    
    return spotify_ids


def music_creation(emotion):
    load_dotenv(dotenv_path="../.env")
    CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
    scope = "user-top-read playlist-modify-public"
    auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
    music = spotipy.Spotify(auth_manager=auth_manager)

    
    
    mood_params = {"happy": {"target_valence": 0.8, "target_energy": 0.8},
                   "sad": {"target_valence": 0.2, "target_energy": 0.3},
                   "angry": {"target_valence": 0.1, "target_energy": 0.9},
                   "neutral": {"target_valence": 0.5, "target_energy": 0.5},
                   "disgust": {"target_valence": 0.1, "target_energy": 0.5}}
    emotion =  emotion
    if emotion is None:
        return
    emotion = emotion.lower()
    if emotion not in mood_params:
        emotion = "neutral"
    targets = mood_params[emotion]

    # time_pref = 'long_term'
    # top_tracks = music.current_user_top_tracks(limit=50, offset=0, time_range=time_pref)
    # track_ids = [track['id'] for track in top_tracks]
    print(mood_params[emotion]["target_energy"])
    df = pd.read_csv("music_genre.csv")
    filtered_df = df[(df['energy'] <= mood_params[emotion]["target_energy"] + 0.1) & (df['valence'] <= mood_params[emotion]["target_valence"] + 0.1 )]
    further_filter = filtered_df[(filtered_df['energy'] >= mood_params[emotion]["target_energy"] - 0.1) &  (filtered_df['valence'] >= mood_params[emotion]["target_valence"] - 0.1 )]
    selected_songs = filtered_df.head(20)

    # Get Spotify track IDs using search API
    track_names = selected_songs["track_name"].tolist()
    artist_names = selected_songs["artist_name"].tolist()
    spotify_track_ids = get_spotify_track_ids(music, track_names, artist_names)

    print((further_filter['instance_id']))
    val_list = list(further_filter['instance_id'].head(20))
    val_list = [int(instance_id) for instance_id in val_list]
    val_list = [str(instance_id) for instance_id in val_list]
    print(val_list)

    user_id = music.current_user()['id']
    playlist_name = "Songs based on face detection"
    playlist_description = "A playlist created using face detection and Spotify API"
    playlist_created = music.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
    
    music.playlist_add_items(playlist_id=playlist_created['id'], items=spotify_track_ids)
    return playlist_created['id']
    print("Playlist created successfully! Check your Spotify.")
    # print("Public playlist created in Spotify account")
    # 
    # 
    # time.sleep(2)
    # 
    # print("Check your spotify app now :) ")
    # playlist_id = playlist_created['id']
    # embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"

    # st.title('Mood Music Recommendation')
    # st.markdown(
    #     f"""
    #     <iframe src="{embed_url}" 
    #     width="400" 
    #     height="600" 
    #     frameborder="0" 
    #     allowtransparency="true" 
    #     allow="encrypted-media"></iframe> 
    #     """,
    #     unsafe_allow_html=True #tested
if __name__ == "__main__":
    val = False
    # username = st.text_input("Enter a unique username:")

    # if username:
    #     cache_path = f".cache_{username}"  # Unique cache per user
        
    #     auth_manager = SpotifyOAuth(
    #         client_id=CLIENT_ID,
    #         client_secret=CLIENT_SECRET,
    #         redirect_uri=REDIRECT_URI,
    #         scope="playlist-modify-public",
    #         cache_path=cache_path
    #     )

    # music = spotipy.Spotify(auth_manager=auth_manager)
    # st.success(f"Logged into Spotify as: {music.current_user()['display_name']}")
    
    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False
    if st.button("Capture Image & Generate Playlist"):
        st.session_state.button_clicked = True
    st.title("Playlist Creation")
    st.write("Get Ready!!! Camera is opening")
    if st.session_state.button_clicked:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if not ret or frame is None or frame.size == 0:
            st.error("No valid image captured! Please check your camera.")
            val = "neutral"
        else:
            st.write("Capturing emotion")
            emotion = emotion_detection()
            st.success(f"Emotion Captured: {emotion}")
            val = music_creation(emotion)
        
    
    

        play_url = f"https://open.spotify.com/embed/playlist/{val}"
        #st.markdown("<br><br><br>", unsafe_allow_html=True) 
        st.markdown(
            f"""
            <iframe src="{play_url}" 
            width="400" 
            height="600" 
            frameborder="0" 
            allowtransparency="true" 
            allow="encrypted-media"></iframe> 
            """,
            unsafe_allow_html=True
        )
        st.success("Playlist created! Enjoy your music! :)")
        if st.button("🔄 Logout from Spotify"):
            if os.path.exists(".cache"):
                os.remove(".cache")
                st.success("Logged out! Please refresh the page and log in again.")

        
print("hi")
import streamlit as st
import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
import time
import cv2
from deepface import DeepFace
# def emotion_detection():
   
#     cam = cv2.VideoCapture(0)
#     ret,frame = cam.read()
#     print(ret)

            
      
            

    # cam.release()
    # if ret == False:
    #     print("No camera detected")
    # else:
    #     enforce_detection=False  
    #     print("Camera detected")
    #     analysis = DeepFace.analyze(frame, actions=['emotion'])
        
    #     print("analysis is a list")
        

    #         # print("analysis is not a list")
    #         # print(analysis)
    #         # print(len(analysis))
    #     trial = analysis[0]
    #         # print("Race analysis:", trial.get("dominant_race"))
    #         # print("Emotion:", trial.get("dominant_emotion"))
    #         # print("Age:", trial.get("age"))
    #         # print("Gender:", trial.get("dominant_gender"))
    #         # print("Age:", analysis.get("age"))
    #         # print("Gender:", analysis.get("gender")
    #     print(trial.get("dominant_emotion"))
    #     return trial.get("dominant_emotion")

def music_creation():
    load_dotenv(dotenv_path="../.env")
    CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
    scope = "user-top-read playlist-modify-public"
    auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
    music = spotipy.Spotify(auth_manager=auth_manager)
    # recs = music.recommendations(seed_genres=["pop"], limit=1)
    try:
        genres = music.recommendation_genre_seeds()['genres']
        print("Available Genres:")
        print(", ".join(genres))
        return genres
    except Exception as e:
        print(f"Error fetching available genres: {e}")
        return []

    print(recs)   
    # mood_params = {"happy": {"target_valence": 0.8, "target_energy": 0.7},
    #                "sad": {"target_valence": 0.2, "target_energy": 0.3},
    #                "angry": {"target_valence": 0.1, "target_energy": 0.9},
    #                "neutral": {"target_valence": 0.5, "target_energy": 0.5},
    #                "disgust": {"target_valence": 0.1, "target_energy": 0.5}}
    # emotion = "happy" # emotion_detection()
    # if emotion is None:
    #     return
    # emotion = emotion.lower()
    # if emotion not in mood_params:
    #     emotion = "neutral"
    # targets = mood_params[emotion]
    # recs = music.recommendations(
    #     seed_genres=["pop"],
    #     limit=10,
    #     target_valence=targets["target_valence"],
    #     target_energy=targets["target_energy"]
    # )
    # user_id = music.current_user()["id"]
    # playlist_name = "Your Mix using face detection"
    # playlist_description = "Created using ML and face detection"
    # playlist_created = music.user_playlist_create(
    #     user=user_id,
    #     name=playlist_name,
    #     public=True,
    #     description=playlist_description
    # )
    # song_links = [track["uri"] for track in recs["tracks"]]
    # music.playlist_add_items(playlist_id=playlist_created["id"], items=song_links)
    # var = 0
    # for track in top_tracks['items']:
    #     track_name = track['name']
    #     artists = ", ".join([artist['name'] for artist in track['artists']])
    #     print(f"{counter}. {track_name} by {artists}")
    #     song_links.append(track['uri'])
    #     counter = counter + 1
    # print("Public playlist created in Spotify account")
    # user_id = music.current_user()['id']
    # playlist_name = "My Top 50 Tracks"
    # playlist_description = f"A playlist of my {time_pref} top 50 tracks via Spotify API"
    # playlist_created = music.user_playlist_create( user=user_id,  name=playlist_name,  public=True,  description=playlist_description )
    # time.sleep(2)
    # music.playlist_add_items(playlist_id=playlist_created['id'], items=song_links)
    # print("Check your spotify app now : ")
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
    #)
if __name__ == "__main__":
    print(music_creation())
    
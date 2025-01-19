# import streamlit as st
# import spotipy
# from dotenv import load_dotenv
# import os
# from spotipy.oauth2 import SpotifyOAuth
# import time
# import cv2
# from deepface import DeepFace
# import pandas as pd
# import numpy as np
# # def emotion_detection():
   
# #     cam = cv2.VideoCapture(0)
# #     ret,frame = cam.read()
# #     print(ret)

            
      
            

#     # cam.release()
#     # if ret == False:
#     #     print("No camera detected")
#     # else:
#     #     enforce_detection=False  
#     #     print("Camera detected")
#     #     analysis = DeepFace.analyze(frame, actions=['emotion'])
        
#     #     print("analysis is a list")
        

#     #         # print("analysis is not a list")
#     #         # print(analysis)
#     #         # print(len(analysis))
#     #     trial = analysis[0]
#     #         # print("Race analysis:", trial.get("dominant_race"))
#     #         # print("Emotion:", trial.get("dominant_emotion"))
#     #         # print("Age:", trial.get("age"))
#     #         # print("Gender:", trial.get("dominant_gender"))
#     #         # print("Age:", analysis.get("age"))
#     #         # print("Gender:", analysis.get("gender")
#     #     print(trial.get("dominant_emotion"))
#     #     return trial.get("dominant_emotion")




# def music_creation():
#     load_dotenv(dotenv_path="../.env")
#     CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
#     CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
#     REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
#     scope = "user-top-read playlist-modify-public"
#     auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope)
#     music = spotipy.Spotify(auth_manager=auth_manager)

    
    
#     mood_params = {"happy": {"target_valence": 0.8, "target_energy": 0.8},
#                    "sad": {"target_valence": 0.2, "target_energy": 0.3},
#                    "angry": {"target_valence": 0.1, "target_energy": 0.9},
#                    "neutral": {"target_valence": 0.5, "target_energy": 0.5},
#                    "disgust": {"target_valence": 0.1, "target_energy": 0.5}}
#     emotion = "happy" # emotion_detection()
#     if emotion is None:
#         return
#     emotion = emotion.lower()
#     if emotion not in mood_params:
#         emotion = "neutral"
#     targets = mood_params[emotion]

#     # time_pref = 'long_term'
#     # top_tracks = music.current_user_top_tracks(limit=50, offset=0, time_range=time_pref)
#     # track_ids = [track['id'] for track in top_tracks]
#     print(mood_params[emotion]["target_energy"])
#     df = pd.read_csv("music_genre.csv")
#     filtered_df = df[(df['energy'] <= mood_params[emotion]["target_energy"] + 0.1) & (df['valence'] <= mood_params[emotion]["target_valence"] + 0.1 )]
#     further_filter = filtered_df[(filtered_df['energy'] >= mood_params[emotion]["target_energy"] - 0.1) &  (filtered_df['valence'] >= mood_params[emotion]["target_valence"] - 0.1 )]
#     print((further_filter['instance_id']))
#     val_list = list(further_filter['instance_id'].head(20))
#     val_list = [int(instance_id) for instance_id in val_list]
#     val_list = [str(instance_id) for instance_id in val_list]
#     print(val_list)

#     user_id = music.current_user()['id']
#     playlist_name = "Songs based on face detection"
#     playlist_description = f"A playlist created using face detection and NLP with Spotify API and Kaggle Dataset"
#     playlist_created = music.user_playlist_create(     user=user_id,      name=playlist_name,     public=True,      description=playlist_description )
#     music.playlist_add_items(playlist_id=playlist_created['id'], items=val_list)

    
    
#     # print("Public playlist created in Spotify account")
#     # 
#     # 
#     # time.sleep(2)
#     # 
#     # print("Check your spotify app now :) ")
#     # playlist_id = playlist_created['id']
#     # embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"

#     # st.title('Mood Music Recommendation')
#     # st.markdown(
#     #     f"""
#     #     <iframe src="{embed_url}" 
#     #     width="400" 
#     #     height="600" 
#     #     frameborder="0" 
#     #     allowtransparency="true" 
#     #     allow="encrypted-media"></iframe> 
#     #     """,
#     #     unsafe_allow_html=True #tested
# if __name__ == "__main__":
#     music_creation()
    

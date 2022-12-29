from bs4 import BeautifulSoup
import requests
import os


CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")


#--------- Song Lists from web scrape-------#
#time = input("Which year you would like to travel to? Type the date in this format YYY-MM-DD")
time = "2020-06-16"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}/")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")


target_list = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
song_list = [target.getText().strip() for target in target_list]



#-----------Spotipy--------#
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

#----------Creating Songs uri list----------#

song_uris = []
year = time.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
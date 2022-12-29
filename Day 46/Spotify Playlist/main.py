from bs4 import BeautifulSoup
import lxml
import requests
import os

CLIENT_ID = os.environ.get("ENV_SPOTIFY_ID")
CLIENT_SECRET = os.environ.get("ENV_SPOTIFY_SECRET")

#time = input("Which year you would like to travel to? Type the date in this format YYY-MM-DD")
time = "2020-06-16"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}/")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")


target_list = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
song_list = [target.getText().strip() for target in target_list]

print(song_list)
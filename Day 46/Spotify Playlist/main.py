from bs4 import BeautifulSoup
import lxml
import requests

CLIENT_ID = "edba50b90dbd4dc58e712e94a4ed9543"
CLIENT_SECRET = "68c5e350360f4a2e812caef54bb05def"

#time = input("Which year you would like to travel to? Type the date in this format YYY-MM-DD")
time = "2020-06-16"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}/")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")


target_list = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
song_list = [target.getText().strip() for target in target_list]

print(song_list)
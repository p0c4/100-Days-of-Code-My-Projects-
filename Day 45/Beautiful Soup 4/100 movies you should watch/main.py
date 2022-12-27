from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

print(soup.title)

all_movies = soup.find_all(name="h3", class_="title")
greatest_movies = [movie.getText() for movie in all_movies]


greatest_movies_reverse = greatest_movies[::-1]

with open("file.txt", "w", encoding="utf-8") as data_file:
    [data_file.write(f"{movie}\n") for movie in greatest_movies_reverse]
    




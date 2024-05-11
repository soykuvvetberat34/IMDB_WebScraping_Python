#Berat SOYKUVVET
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.186 Safari/537.36'
}
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

response = soup.find("ul", {"class": "ipc-metadata-list"}).find_all("li")

for item in response:
    filmName=item.find("h3").text
    filmScore=item.find("span",{"class":"ipc-rating-star"}).text
    print(filmName,filmScore)

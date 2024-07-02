import requests
from bs4 import BeautifulSoup


def download_anime(anilink):
    r = requests.get(anilink+'ep-1')
    soup = BeautifulSoup(r.content, 'html.parser')
    eps = soup.find_all('span', class_='d-title')
    print(eps)
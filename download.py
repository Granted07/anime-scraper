import requests
from bs4 import BeautifulSoup


def download_anime(anilink):
    r = requests.get(anilink)
    soup = BeautifulSoup(r.content, 'html.parser')
    eps = soup.find_all('ul', class_='ep-range')
    f = open('allspan.html','w')
    f.write(soup.prettify())
    f.close()
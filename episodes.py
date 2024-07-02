import requests
from bs4 import BeautifulSoup


def download_anime(gogolink):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0.'}
    r = requests.get(gogolink,timeout=10)
    # requests.session().close()
    soup = BeautifulSoup(r.content, 'html.parser')
    eps = soup.find_all('div', class_='name')
    for i in eps:
        print(i.get_text())
import requests
from bs4 import BeautifulSoup
from download import get_download_link


def find_ep(gogolink):
    global r
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0.'}
    f = True
    while f:
        try:
            r = requests.get(gogolink, timeout=10, headers=headers)
            f = 0
        except:
            continue
    soup = BeautifulSoup(r.content, 'html.parser')
    eps = soup.find_all('div', class_='anime_video_body')[0].find('a').getText().split('-')
    get_download_link(int(input(f'\033[0mEnter Episode (\033[1;34;20m{int(eps[0]) + 1}-{int(eps[1])}\033[0m): \033[1;32;20m')), gogolink)

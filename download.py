import requests
from bs4 import BeautifulSoup


def get_download_link(epNumber,gogolink):
    global search_source
    link = gogolink.replace('category/','') + '-episode-'+ str(epNumber)
    print(link)
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    f = True
    while f:
        try:
            search_source = requests.get(link, timeout=10, headers=headers)
            f = 0
        except:
            continue
    soup = BeautifulSoup(search_source.text, 'html.parser')
    downlink = soup.find('li', class_='dowloads').find('a')['href']
    open('test.html', 'w', encoding='utf-8').write(str(downlink))
    print(downlink)



import os

try:
    import requests, ffmpeg, selenium
    from bs4 import BeautifulSoup
except:
    print('installing modules...')
    os.system('pip install -r requirement.txt')
    import requests
    from bs4 import BeautifulSoup

from episodes import find_ep

titles = {}


def find_title(soupfn):
    find_soup = soupfn.find_all('p', class_='name', )
    for i in find_soup:
        # print(i)
        for j in i.find_all('a'):
            titles[j.get_text()] = j.attrs['href']
    return titles


search = input('Enter searched anime: ')
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148'}
link = 'https://gogoanime3.co/search.html?keyword=' + search
f = True
while f:
    try:
        search_source = requests.get(link, timeout=10, headers=headers)
        f = 0
    except:
        continue
soup = BeautifulSoup(search_source.content, 'html.parser')
titles = find_title(soup)
for i in range(len(titles.keys())):
    try:
        print(f'[{i + 1}]', list(titles.keys())[i])
    except:
        break
choice = input(f"Please Choose (1-{i+1}): ")
gogolink = 'https://gogoanime3.co' + titles[list(titles.keys())[int(choice) - 1]]
find_ep(gogolink)



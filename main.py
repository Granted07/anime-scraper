import os
import sys

from episodes import find_ep

try:
    import requests
    from bs4 import BeautifulSoup
except:
    print('installing modules...')
    os.system('python -m pip install requests beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup

# check status code for response received
# success code - 200

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
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
link = 'https://gogoanime3.co/search.html?keyword=' + search
f = True
while f:
    try:
        search_source = requests.get(link, timeout=10, headers=headers)
        f = 0
    except:
        continue
# time.sleep(5)
soup = BeautifulSoup(search_source.content, 'html.parser')
titles = find_title(soup)
# f = open('allspan.html','w')
# f.write(str(titles))
# f.close()
for i in range(9):
    try:
        print(f'[{i + 1}]', list(titles.keys())[i])
    except:
        break
choice = input("Please Choose (1-9):")
gogolink = 'https://gogoanime3.co' + titles[list(titles.keys())[int(choice) - 1]]
print(gogolink)
find_ep(gogolink)

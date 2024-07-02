import os
import sys
import time

from episodes import download_anime

# from download import download_anime

try:
    import requests
    from bs4 import BeautifulSoup
except:
    print('installing modules...')
    os.system('python -m pip install requests beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup

# Making a GET request

# check status code for response received
# success code - 200
# print(r)
# pageurl = https://aniwavetv.to/home
# print content of request

titles = {}


def find_title(soupfn):
    find_soup = soupfn.find_all('p', class_='name', )
    for i in find_soup:
        # print(i)
        for j in i.find_all('a'):
            titles[j.get_text()]=j.attrs['href']
    return titles


# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find('input').attrs)

if sys.argv[1] == '-s':
    search = sys.argv[2].replace(' ', '+')
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    link = 'https://gogoanime3.co/search.html?keyword=' + search
    try:
        search_source = requests.get(link, timeout=10, headers=headers)
        # requests.session().close()
    except Exception as e:
        print(e)
        exit()
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
    download_anime(gogolink)
    #
    # r = requests.get(link, timeout=10, headers=headers)
    # soup = BeautifulSoup(r.content, 'html.parser')
    # eps = soup.find_all('div', class_='name')
    # for i in eps:
    #     print(i.get_text())

# print(soup.prettify())
# attributes_dictionary = soup.find('div').attrs

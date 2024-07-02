import os
import sys
import time

# from download import download_anime

try:
    import requests
    from bs4 import BeautifulSoup
except:
    print('installing modules...')
    os.system('python -m pip install requests beautifulsoup4')

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
    link = 'https://gogoanime3.co/search.html?keyword=' + search
    requests.get(link).close()
    search_source = requests.get(link, timeout=10)
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
    anilink = 'https://gogoanime3.co'+titles[list(titles.keys())[int(choice)-1]]
    # download_anime(anilink)
    print(anilink)
# print(soup.prettify())
# attributes_dictionary = soup.find('div').attrs

import os
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except:
    print('installing modules...')
    os.system('python -m pip install requests beautifulsoup4')

# Making a GET request
r = requests.get('https://aniwavetv.to/home')

# check status code for response received
# success code - 200
# print(r)
# pageurl = https://aniwavetv.to/home
# print content of request

titles = {}


def find_title(soup):
    find_soup = soup.find_all('a', class_='d-title')
    for i in find_soup:
        titles[i.text] = i.attrs['href']
    return titles


# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find('input').attrs)

if sys.argv[1] == '-s':
    search = sys.argv[2].replace(' ', '+')
    link = 'https://aniwavetv.to/filter?keyword=' + search
    search_source = requests.get(link)
    soup = BeautifulSoup(search_source.content, 'html.parser')
    titles = find_title(soup)
    for i in range(9):
        print(f'[{i + 1}]', list(titles.keys())[i])
    choice = input("Please Choose (1-9):")
    print('https://aniwavetv.to'+titles[list(titles.keys())[int(choice)-1]])


# print(soup.prettify())
# attributes_dictionary = soup.find('div').attrs

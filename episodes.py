import os

from download import get_download_link

try:

    import requests
    from bs4 import BeautifulSoup
except:
    print('installing modules...')
    os.system('python -m pip install requests beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup



def find_ep(gogolink):
    global r
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:110.0) Gecko/20100101 Firefox/110.0.'}
    f = True
    while f:
        try:
            s=requests.session()
            r = s.get(gogolink, timeout=10, headers=headers)
            s = requests.session()
            s.get('https://s3taku.com')
            cookies = s.cookies.get_dict()
            s = requests.session()
            s.get('https://www.google.com')
            cookiesg = s.cookies.get_dict()
            f = 0
        except:
            continue
    # requests.session().close()
    soup = BeautifulSoup(r.content, 'html.parser')
    eps = soup.find_all('div', class_='anime_video_body')[0].find('a').getText().split('-')
    get_download_link(int(input(f'Enter Episode ({int(eps[0])+1}-{int(eps[1])}): ')),gogolink,cookies,cookiesg)

    # open('test.html', 'w', encoding="utf-8").write(soup.prettify())

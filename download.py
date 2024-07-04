import os, time, re
import subprocess
import sys

from progress import print_progress_bar

# from progress import print_progress_bar


def download(episodenumber, r):
    total_length = (int(r.headers.get('Content-Length'))) // 1024 ** 2
    print("Downloading...")
    print_progress_bar(0, total_length + 1, prefix='Progress:', suffix='Complete', length=50)
    i = 0
    with open(str(episodenumber) + '.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 ** 2):
            if chunk:
                i += 1
                print_progress_bar(i, total_length, prefix='Progress:', suffix='Complete', length=50)
                f.write(chunk)
                f.flush()

def stream(r):
    with open(str('7.mp4') + '.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=4000 ** 2):
            if chunk:
                f.write(chunk)
                f.flush()
                time.sleep(1)
                try:
                    os.startfile('7.mp4')
                except:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    subprocess.call([opener, '7.mp4'])



try:
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from clint.textui import progress
except:
    print('installing modules...')
    os.system('pip install -r requirement.txt')
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from clint.textui import progress


def get_download_link(epNumber, gogolink):
    global search
    link = gogolink.replace('category/', '') + '-episode-' + str(epNumber)
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Mobile/15E148'}
    f = True
    while f:
        try:
            search = requests.get(link, timeout=10, headers=headers)
            f = 0
        except:
            continue
    soup = BeautifulSoup(search.text, 'html.parser')
    # downlink = soup.find('li', class_='vidcdn').find('a')['data-video']
    # content = requests.get(downlink).content
    # soup = remove_tags(content)
    # open('test.html', 'w').write(soup)
    downlink = soup.find('li', class_='dowloads').find('a')['href']
    download_episode(downlink, epNumber)


def download_episode(link, episodenumber):
    print("Fetching Download Options, please wait a sec...")
    global j, html
    options = webdriver.FirefoxOptions()
    # options.add_argument("-profile")
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    # wait = WebDriverWait(driver, 100)
    driver.get(link)
    time.sleep(1.5)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    driver.quit()
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')
    dows = soup.findAll('div', class_='dowload')
    c = 0
    for links in dows:
        dowopts = links.find('a').text.replace('\n', '')
        if dowopts[-4:-1] == 'mp4':
            c += 1
            if dowopts[-12] in ' -)(':
                print(f"[{c}] {dowopts[-11:-7]}")
            else:
                print(f"[{c}] {dowopts[-12:-7]}")
        else:
            break
    qchoice = int(input(f"Enter a download option (1-{c}): "))
    schoice = int(input("[1] Stream\n[2] Download\nEnter an option (1-2): "))
    url = dows[qchoice].find('a').attrs['href']
    print(url)
    r = requests.get(url, stream=True)
    if schoice == 1:
        stream(r)
    else:
        download(episodenumber,r)

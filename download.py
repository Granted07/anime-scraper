import time
import subprocess
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from progress import print_progress_bar


def download(episode_number, r):
    total_length = (int(r.headers.get('Content-Length'))) // 1024 ** 2
    print("Downloading...")
    print_progress_bar(0, total_length + 1, prefix='Progress:', suffix='Complete', length=50)
    i = 0
    with open(str("Episode " + str(episode_number)) + '.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 ** 2):
            if chunk:
                i += 1
                print_progress_bar(i, total_length, prefix='Progress:', suffix='Complete', length=50)
                f.write(chunk)
                f.flush()


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
    downlink = soup.find('li', class_='dowloads').find('a')['href']
    download_episode(downlink, epNumber)


def download_episode(link, episodenumber):
    print("\033[1;36;20mFetching Download Options, please wait a sec...")
    global j, html
    service = Service()
    try:
        browser: int = int(open('/installed-browser.txt', 'r').read().split('\n')[0][-1])
    except:
        browser: int = 1
    if browser == 1:
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options, service=service)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("-headless")
        driver = webdriver.Chrome(service=service, options=options)
    driver.get(link)
    time.sleep(1.5)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    dows = soup.findAll('div', class_='dowload')
    c = 0
    for links in dows:
        dowopts = links.find('a').text.replace('\n', '')
        if dowopts[-4:-1] == 'mp4':
            c += 1
            if dowopts[-12] in ' -)(':
                print(f"\033[1;34;20m[{c}] \033[1;35;20m{dowopts[-11:-7]}")
            else:
                print(f"\033[1;34;20m[{c}] \033[1;35;20m{dowopts[-12:-7]}")
        else:
            break
    q_choice = int(input(f"\033[0mEnter a download option (\033[1;34;20m1-{c}\033[0m): \033[1;32;20m"))
    if os.name == 'nt':
        s_choice = int(input("\033[1;34;20m[1] \033[1;35;20mStream (vlc is required in default Program Files x86 "
                             "folder)\n\033[1;34;20m[2] \033["
                             "1;35;20mDownload\n\033[0mEnter an option (\033[1;34;20m1-2\033[0m): "))
    else:
        s_choice = int(input("\033[1;34;20m[1] \033[1;35;20mStream (vlc required)\n\033[1;34;20m[2] \033["
                             "1;35;20mDownload\n\033[0mEnter an option (\033[1;34;20m1-2\033[0m): "))
    url = dows[q_choice].find('a').attrs['href']
    r = requests.get(url, stream=True)
    if s_choice == 1:
        if os.name == 'nt':
            subprocess.Popen([r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe', url])
        else:
            subprocess.Popen(['vlc', url])
    else:
        download(episodenumber, r)

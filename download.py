import time
# import selenium
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def get_download_link(epNumber, gogolink):
    global search_source
    link = gogolink.replace('category/', '') + '-episode-' + str(epNumber)
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
    download_episode(downlink)


def download_episode(link,):
    global j
    dowkeys, dowvalues = [], []
    options = webdriver.FirefoxOptions()
    # options.add_argument("-profile")
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    # wait = WebDriverWait(driver, 100)
    driver.get(link)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    driver.quit()
    # print(html)
    open('test.html', 'w', encoding='utf-8').write(str(html))
    # f = True
    # while f:
    #     try:
    #         s = requests.Session()
    #         search_source = s.get(link, timeout=10, allow_redirects=True)
    #         time.sleep(5)
    #         f = 0
    #     except:
    #         continue
    soup = BeautifulSoup(html, 'html.parser')
    i = soup.findAll('div', class_='dowload')
    for j in i:
        dowkeys.append(j.find('a').text.split())
        dowvalues.append(j.find('a').attrs['href'])
    dowdict = dict(zip(dowkeys, dowvalues))
    for i in dowdict:
        print(f"{i}= {dowdict[i]}")
    # print(dowclass[0])

    # print(downlink, "\n", type(downlink))

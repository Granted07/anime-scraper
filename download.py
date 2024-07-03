
import os,time

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
            print(f"[{c}] {dowopts}")
        else:
            break
    qchoice = int(input(f"Enter a a download option (1-{c}): "))
    print("Downloading...")
    url = dows[qchoice].find('a').attrs['href']
    r = requests.get(url)
    with open(str(episodenumber)+'.mp4', 'wb') as f:
        total_length = int(r.headers.get('Content-Length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

import os

try:
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
except:
    print('installing modules...')
    os.system('python -m pip install requests beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver

def get_download_link(epNumber, gogolink):
    global search
    link = gogolink.replace('category/', '') + '-episode-' + str(epNumber)
    print(link)
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
    open('test.html', 'w', encoding='utf-8').write(str(downlink))
    print(downlink)
    download_episode(downlink, epNumber)


def download_episode(link, episodenumber):
    global j
    options = webdriver.FirefoxOptions()
    # options.add_argument("-profile")
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    print("Fetching Download Options, please wait a sec...")
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
    r = requests.get(dows[qchoice].find('a').attrs['href'], allow_redirects=True)
    print("Downloading...")
    open(str(episodenumber) + '.mp4', 'wb').write(r.content)

    # dowvalues.append(j.find('a'))
    # print(dowclass[0])
    # print(downlink, "\n", type(downlink))

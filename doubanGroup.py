from urllib import request
from bs4 import BeautifulSoup
import time

for i in range(0, 353):
    url = 'https://www.douban.com/group/explore?start=' + str(i*30)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    bf = BeautifulSoup(html)
    ls = bf.find_all('div', class_="channel-item")
    for el in ls:
        el_bf = BeautifulSoup(str(el))
        title = el_bf.find('h3').get_text()
        desc = el_bf.find('p').get_text()

        with open('豆瓣.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')  
            f.write(desc)
            f.write('\n------------------------------------\n')
    time.sleep(2)
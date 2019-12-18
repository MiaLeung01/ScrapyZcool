import requests, sys, time, re, os
from bs4 import BeautifulSoup
from contextlib import closing

"""
类说明： 爬取zc图片

说明： 先获取主页中的各个小模块的 html 连接，然后从该 html 中获取到 objectId，
一个 objectId 可以获取到相应图片地址
存储的时候，会生成对应主题的文件夹，里面放相应的图片
"""

class Downloader():
    def __init__(self, proxy={'http':'223.198.21.225'}):
        self.page_url = {}
        self.user_urls = []
        self.proxies = proxy  

    def startTask(self, page):
        url = 'https://www.zcool.com.cn/?p=' + str(page)
        self.getPageUrl(url)
        for val in self.page_url.values():
            if not os.path.exists(val['path']):
                os.mkdir(val['path'])
            imgs = self.getImgsUrl(val['objid'])
            for i in range(len(imgs)):
                self.saveImg(imgs[i], val['path'], i)

    def getPageUrl(self, url, rpath= r'D:\Company\explore\res'):
        req = requests.get(url, proxies=self.proxies)
        bf = BeautifulSoup(req.text)
        try:
            div_bf = BeautifulSoup(str(bf.find_all('div', class_='work-list-box')[0]))
            a = div_bf.find_all('a', class_='title-content')
            for item in a:
                href = item['href']
                title = re.sub(r'[\/:*?"<>|]*', '' , item['title'].strip())
                path = rpath + '/' + title
                # 匹配 work 下的页面
                match = re.match('https://www.zcool.com.cn/work/', href)
                if(match):
                    # 为了判断当前url里不包含图片文件夹
                    self.getPageUrl(href, path)
        # 最小单位才放入
        except IndexError: 
            objid = self.getPageObjectIdAndTitle(url)
            if(objid):
                self.page_url[url] = {
                    'objid': objid,
                    'path': rpath  # 存储路径
                }
                print({
                    'objid': objid,
                    'path': rpath
                })       
        

    # 从页面 html  在 id='dataInput' 的 data-objid 属性中 拿到 objectId:
    def getPageObjectIdAndTitle(self, url):
        req = requests.get(url, proxies=self.proxies)
        bf = BeautifulSoup(req.text)
        if(bf.find_all(id='dataInput')):
            objid = bf.find_all(id='dataInput')[0]['data-objid']
            return objid
        else:
            return None

    # 根据 objectId 获取当前页面的图片地址
    def getImgsUrl(self, objectId):
        url = 'https://www.zcool.com.cn/work/content/show?objectId='+str(objectId)
        req = requests.get(url, proxies=self.proxies)
        img_links = []
        for item in req.json()['data']['allImageList']:
            img_links.append(item['url'])
        return img_links

    # 根据图片地址存储到本地
    def saveImg(self, url, path, name):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        p = str(path) + '/' + str(name) + '.jpg'
        if os.path.exists(p):
            print('文件存在，跳过')
            return
        with closing(requests.get(url, stream=True, verify = False, headers = headers)) as r:
            with open(p, 'ab+') as f:
                for chunk in r.iter_content(chunk_size = 1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            time.sleep(2)


if __name__ == "__main__":
    dl = Downloader()
    #从第1页到第100页
    for page in range(1,101):
        print('开始爬取第%d页'%page)
        dl.startTask(page)

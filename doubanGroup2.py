# import requests, threading, time
# from bs4 import BeautifulSoup

# # python 爬虫小白教程 2 - 多线程爬取

# def get_page_info(url, ):
#     print('线程', threading.current_thread().name, '开始')
#     headers = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
#     }
#     proxy={'http':'163.204.242.181:9999'}
#     req = requests.get(url=url, headers=headers, proxies=proxy)  
#     bf = BeautifulSoup(req.text)
#     ls = bf.find_all('div', class_="channel-item")
#     print('线程', threading.current_thread().name, '写入')
#     for el in ls:
#         el_bf = BeautifulSoup(str(el))
#         title = el_bf.find('h3').get_text()
#         desc = el_bf.find('p').get_text()
#         with open('豆瓣.txt', 'a', encoding='utf-8') as f:
#             f.write(title)
#             f.write('\n')  
#             f.write(desc)
#             f.write('\n------------------------------------\n')
#     print('线程', threading.current_thread().name, '完成')
#     time.sleep(2)

# if __name__ == '__main__':
#     start_time = time.time()
#     for i in range(0, 353):
#         url = 'https://www.douban.com/group/explore?start=' + str(i*30)
#         t = threading.Thread(target=get_page_info,args=(url, ), name=str(i))
#         t.start()
#         t.join()
#     end_time = time.time()
#     print('一共花费', str(end_time - start_time), '秒')
    


# python 爬虫小白教程 2 - 代理设置与多进程爬取

import requests, time, random
from bs4 import BeautifulSoup
from multiprocessing import Pool


#代理列表：
plist = [
    '123.163.122.247:9999'
    '223.199.18.59:9999'
    '223.199.22.177:9999'
]

def get_page_info(url,name):
    print('进程', name, '开始')
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    proxy = {'https': random.choice(plist)}
    req = requests.get(url=url, headers=headers, proxies=proxy)  
    bf = BeautifulSoup(req.text, 'lxml')
    ls = bf.find_all('div', class_="channel-item")
    # print('进程', name, '写入', req.text)
    for el in ls:
        el_bf = BeautifulSoup(str(el))
        title = el_bf.find('h3').get_text()
        desc = el_bf.find('p').get_text()
        with open('123.txt', 'a', encoding='utf-8') as f:
            f.write(title)
            f.write('\n')  
            f.write(desc)
            f.write('\n------------------------------------\n')
    print('进程', name, '完成')
    time.sleep(2)

if __name__ == '__main__':
    start_time = time.time()

    p = Pool(20)
    for i in range(0, 5):
        url = 'https://www.douban.com/group/explore?start=' + str(i*30)
        p.apply_async(get_page_info, (url,str(i) ))
    p.close()
    p.join()
    end_time = time.time()
    print('一共花费', str(end_time - start_time), '秒')
    
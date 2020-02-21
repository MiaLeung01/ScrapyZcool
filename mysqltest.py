# python 爬虫小白教程 1 - 爬取豆瓣的话题
from urllib import request
from bs4 import BeautifulSoup
import time, pymysql


# 数据库相关
conn = pymysql.connect(host='127.0.0.1', port=3306, 
    user='root',passwd='123456', db='sp',charset='utf8mb4')
cursor = conn.cursor() 

for i in range(0, 353):
    url = 'https://www.douban.com/group/explore?start=' + str(i*30)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    bf = BeautifulSoup(html, 'lxml')
    ls = bf.find_all('div', class_="channel-item")
    for el in ls:
        el_bf = BeautifulSoup(str(el), 'lxml')
        title = el_bf.find('h3').get_text()
        desc = el_bf.find('p').get_text()


    # 存入数据库
    sql = """
        INSERT INTO douban (title, content) VALUES ('%s', '%s') 
    """%(title, desc)
    
    cursor.execute(sql)
    conn.commit()

    sql2 = "SELECT * FROM douban;"
    cursor.execute(sql2)
    print(cursor.fetchall())


    time.sleep(2)



from selenium import webdriver
import time
from bs4 import BeautifulSoup


# options = webdriver.ChromeOptions()
# options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
bs = webdriver.Chrome('E:\chromedriver.exe')
bs.get('https://www.zcool.com.cn/work/ZNDIwMTA2NDg=.html')


# 检查是否滚动到底部, 如果相减结果大于100像素，就认为到还没到底部
r = bs.execute_script("return (document.documentElement.scrollHeight-document.documentElement.scrollTop-document.documentElement.clientHeight)>100")

# 如果没有滚动到底部
while r:
    #向下滚动 1000 像素
    bs.execute_script("window.scrollBy(0, 1000)")
    
    # 暂停 1 秒
    time.sleep(1)
    
    # 重新判断是否滚动到底部
    r = bs.execute_script("return (document.documentElement.scrollHeight-document.documentElement.scrollTop-document.documentElement.clientHeight)>100")


html = bs.page_source
bf = BeautifulSoup(html, 'lxml')
imgs = bf.select('.reveal-work-wrap img')
print(imgs, len(imgs))



# ## 获取阴阳师图片

# # 打开阴阳师页面
# bs.get('https://yys.163.com/shishen/index.html')

# html = bs.page_source
# bf = BeautifulSoup(html, 'lxml')

# # 获取所有 class= "shishen_item" 的​ img 标签
# imgs = bf.select('.shishen_item img')
# print(imgs)

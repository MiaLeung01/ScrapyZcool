import time
import ddddocr
import os
import random
import requests
from PIL import Image

def git_captcha_crack(element, captchlen, imglen):
  try:
    captcha_codes = []
    for i in range(imglen):
      code = normal_captcha_crack(element)
      captcha_codes.append(code)
      time.sleep(1)
  except Exception as e:
    print('captcha img error',e)
  try:
    maparr = []
    for i in range(len(captcha_codes)):
      if (len(captcha_codes[i]) >= captchlen):
        for j, character in enumerate(captcha_codes[i]) :
          if len(maparr) <= j:
            maparr.append({
              character: 1
            })
          else:
            if character in maparr[j]:
              maparr[j][character] += 1
            else:
              maparr[j][character] = 1
    print(maparr)
    result = []
    for map in maparr:
      arr = list(map.values())
      index = arr.index(max(arr))
      ka = list(map.keys())
      result.append(ka[index])
    print(''.join(result[0:captchlen]))
    return ''.join(result[0:captchlen])
  except Exception as e:
    print('git_captcha_crack Error', e)


# 识别图片验证码
def normal_captcha_crack(element):
  # 通过Image处理图像
  filename = os.getcwd() + '\\' + str(random.random()) + '.png'  # 生成随机文件名
  print (filename)
  # driver.save_screenshot(filename)  # 截取当前窗口并保存图片
  element.screenshot(filename)  # 截取当前窗口并保存图片
  im = Image.open(filename)  # 打开图片
  # im = im.crop((left, top, right, bottom))  # 截图验证码
  im.save(filename)  # 保存验证码图片
  # 由于我处理的验证码图片没有填多的线条，所以直接采用灰度是验证码数字更加清晰，具体的处理方式可根据验证码的实际情况而定
  im = Image.open(filename)
  # 转换为灰度图像
  im = im.convert('L')
  im.save(filename)
  # 读取图片，应为字节流
  with open(filename, 'rb')as f:
    image = f.read()
  print(im)
  ocr = ddddocr.DdddOcr()
  res = ocr.classification(image)
  print(res)
  return res


def crackCaptcha(imgUrl):
  headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
  img_bytes = requests.get(imgUrl, headers).content
  
  print(img_bytes)
  ocr = ddddocr.DdddOcr()
  res = ocr.classification(img_bytes)
  print(res)
  return res


from selenium.common.exceptions import NoSuchElementException
def is_pick(self):
  try:
    pick_img = self.browser.find_element_by_css_selector('img.geetest_item_img')
    return pick_img
  except NoSuchElementException:
    return False

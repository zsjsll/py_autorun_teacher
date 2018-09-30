import codecs
import time
import urllib.request as tran
from lxml import etree
from selenium import webdriver
from baiduOCR import OCR
from PIL import Image
# from bs4 import BeautifulSoup

chromeOptions = webdriver.ChromeOptions()
browser = webdriver.Chrome(
    executable_path='D:/py_autorun_teacher/chromedriver/chromedriver.exe',
    chrome_options=chromeOptions)

myUsername = "输入用户名"
myPassword = "输入密码"

browser.get(
    "http://luliang2018.w.px.teacher.com.cn/userIndex/12605181/student")
browser.implicitly_wait(20)
time.sleep(1)

# 填写账号
username = browser.find_element_by_id("username")
username.clear()
username.send_keys(myUsername)

# 填写密码
password = browser.find_element_by_id("password")
password.clear()
password.send_keys(myPassword)

# 获取验证码
code = browser.find_element_by_id("inputvalcode")
code.click()

# 获取验证码图片

#通过获取src的方法来取得图片是不行的，每次取得的验证码和实际验证码不一致
# code_element = browser.find_element_by_css_selector("img[id='validateCode']")
# code_url = code_element.get_attribute("src")
# print(code_url)

#通过截图的方式来获取验证码
f = r'/autorun/code/code.png'
browser.save_screenshot(f)
#获取图片坐标
code_element = browser.find_element_by_css_selector('img[id="validateCode"]')
#左上坐标
element_left = code_element.location['x']
element_top = code_element.location['y']
#右下坐标
element_right = element_left + code_element.size['width']
element_bottom = element_top + code_element.size['height']

picture = Image.open(f)
picture = picture.crop((element_left, element_top, element_right,
                        element_bottom))
picture.save(f)

#调用百度OCR
baidu = OCR()
code_str = baidu.get_pic_str(dir_pic=f)

#输入验证码
code.send_keys(code_str)
#提交表单
submit = browser.find_element_by_css_selector('a[class="_submit"]')
submit.click()

time.sleep(7)

# li = browser.find_elements_by_class_name('wb--')

# li[5].click()

num = 0
ls = browser.find_elements_by_css_selector('ul a[title][href]')
for x in ls:
    tit = x.get_attribute('title')
    print(f"{num}:{tit}")
    num += 1

uuu = ls[50].get_attribute('href')
print(uuu)
browser.get(uuu)
time.sleep(1)

learn = browser.find_element_by_css_selector(
    'a[href][target="frm_course_learn"][class="button-hui"]')
learn.click()

#切换selenium窗口
browser.switch_to_window(browser.window_handles[1])
time.sleep(5)
#点击弹出认证窗口
div = browser.find_element_by_css_selector("#btn_min")
div.click()

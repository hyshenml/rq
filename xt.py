# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep
import cookielib
from cookie import copy_cookie
import urllib2

def save_pic(pic):
    path = ".\\img"
    name = path + "\\1.jpg"
    f = open(name, 'wb')
    f.write(pic)
    f.close()
    print('Pic Saved!')

driver = webdriver.PhantomJS()
#driver = webdriver.PhantomJS(executable_path="E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get('http://wcm.yundasys.com:65216/wcm/login.html')
pass_img_url=driver.find_elements_by_id('imgCode')[0].get_attribute('src')
name_input=driver.find_elements_by_id('username')
pass_input=driver.find_elements_by_id('password')
code_input=driver.find_elements_by_id('passcode')
print pass_img_url

with copy_cookie(driver) as f:
    cookie = f.cookieJar
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open(pass_img_url)
    save_pic(response.read())

img_code=raw_input('code:')
code_input[0].send_keys(img_code)
#name=raw_input('name:')
name_input[0].send_keys('91004')
passwd=raw_input('pass:'t
pass_input[0].send_keys(passwd)
button=driver.find_elements_by_class_name('btn')[0]
actions = ActionChains(driver)
actions.click(button)
actions.perform()
t=driver.find_element_by_id('errorMsg')
sleep(3)
print driver.current_url




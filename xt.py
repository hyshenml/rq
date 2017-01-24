# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep
driver = webdriver.PhantomJS()
driver.get('http://wcm.yundasys.com:65216/wcm/login.html')
pass_img_url=driver.find_elements_by_id('imgCode')[0].get_attribute('src')
name_input=driver.find_elements_by_id('username')
pass_input=driver.find_elements_by_id('password')
code_input=driver.find_elements_by_id('passcode')
print pass_img_url
img_code=raw_input('code:')
code_input[0].send_keys('img_code')
name=raw_input('name:')
name_input[0].send_keys('name')
passwd=raw_input('pass:')
pass_input[0].send_keys('passwd')
button=driver.find_elements_by_class_name('btn')[0]
actions = ActionChains(driver)
actions.click(button)
actions.perform()
sleep(5)
t=driver.find_element_by_link_text(u'报工时')
print t
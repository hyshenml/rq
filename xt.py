# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
driver = webdriver.PhantomJS()
driver.get('http://wcm.yundasys.com:65216/wcm/login.html')
pass_img_url=driver.find_elements_by_id('imgCode')[0].get_attribute('src')
print pass_img_url
img_code=raw_input('code:')
name_input=driver.find_elements_by_id('username')
pass_input=driver.find_elements_by_id('password')
code_input=driver.find_elements_by_id('passcode')
print name_input,pass_input,code_input
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4


browser = webdriver.Firefox(executable_path='/home/davi/Downloads/geckodriver')
browser.get('https://www.facebook.com/')
email = browser.find_element_by_id('email')
email.send_keys('my_email')
passwd = browser.find_element_by_id('pass')
passwd.send_keys('my_password')
passwd.submit()
time.sleep(10)




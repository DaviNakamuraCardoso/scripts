from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/davi/.config/google-chrome/Default')
options.add_argument('--profile-directory=Default')

browser = webdriver.Chrome(executable_path='/home/davi/Downloads/chromedriver_linux64/chromedriver', options=options)

browser.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(3)
button = browser.find_element_by_link_text('Iniciar sessão')
button.click()
time.sleep(2)
email = browser.find_element_by_tag_name('input')
email.send_keys('davinakamuracardoso')
time.sleep(2)
passwd = browser.find_element_by_id('pass')
time.sleep(3)
passwd.send_keys('F22Raptor123')
passwd.submit()
time.sleep(10)





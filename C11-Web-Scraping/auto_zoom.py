import bs4
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/davi/.config/google-chrome/Default')
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='/home/davi/Downloads/chromedriver_linux64/chromedriver', options=options)
driver.get('https://web.whatsapp.com')
time.sleep(10)
search_bt = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bt.click()
search_bt.send_keys('Cong. Central')
search_bt.send_keys(Keys.ENTER)
time.sleep(1)
link = driver.find_elements_by_tag_name('a')
link[-1].click()
time.sleep(2)
pyautogui.click(500, 500, button='left')
time.sleep(7)
pyautogui.press('tab', presses=3, interval=4)
time.sleep(2)
pyautogui.press('enter')


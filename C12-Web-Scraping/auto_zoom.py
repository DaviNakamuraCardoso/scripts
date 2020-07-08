#! /usr/bin/python3

import bs4
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
import re
import sys

actions = {'reuniao': 'reuniao', 'campo': 'campo desta', 'servico': 'servico'}
senha_re = re.compile(r'(Senha:|Password:)(\s)(.*)', re.IGNORECASE)
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/davi/.config/google-chrome/Default')
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='/home/davi/Downloads/chromedriver_linux64/chromedriver', options=options)
driver.get('https://web.whatsapp.com')

time.sleep(5)
pyautogui.click(500, 500, button='left')
time.sleep(1)
search_bt = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bt.click()
search_bt.send_keys('Cong. Central')
search_bt.send_keys(Keys.ENTER)
time.sleep(1)
search_in_gp = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[1]/div/span')
search_in_gp.click()
text_area = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/div/div[1]/div/label')
text_area.click()
pyautogui.typewrite(actions[sys.argv[1]])
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(800, 400)
time.sleep(2)
pyautogui.dragTo(800, 650)
time.sleep(3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
msg = str(pyperclip.paste())
time.sleep(1)
mo = senha_re.search(msg)
senha = str(mo.group(3))
time.sleep(1)
link = driver.find_elements_by_tag_name('a')
link[-1].click()
time.sleep(2)
pyautogui.click(500, 500, button='left')
time.sleep(4)
pyautogui.press('tab', presses=3, interval=1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite(senha)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(700, 600, button='left')
pyautogui.press('tab', presses=3, interval=1)
pyautogui.press('enter')

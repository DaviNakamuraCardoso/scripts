from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

user_name = input('Contato: ')
mensagem = input('Mensagem: ')
n = int(input('Número de vezes: '))
time.sleep(3)
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/davi/.config/google-chrome/Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path='/home/davi/Downloads/chromedriver_linux64/chromedriver', options=options)
driver.get('https://web.whatsapp.com/')
time.sleep(12)
search_bt = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bt.click()
search_bt.send_keys(user_name)
search_bt.send_keys(Keys.ENTER)
time.sleep(1)
#user_name = user_name.split()
#user_name = '&nbsp;&nbsp;'.join(user_name)
#src = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
#src.send_keys('mae')
#src.submit()
time.sleep(1)
for i in range(n):
    text_area = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    text_area.click()
    text_area.send_keys(mensagem)
    send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    send_button.click()
    time.sleep(.5)


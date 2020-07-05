from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/home/davi/Downloads/chromedriver_linux64/chromedriver')
driver.get('https://web.whatsapp.com/')
time.sleep(15)
#src = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
#src.send_keys('mae')
#src.submit()
time.sleep(1)
mae_bt = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span')
time.sleep(1)
mae_bt.click()
time.sleep(1)

for i in range(500):
    text_area = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    text_area.click()
    text_area.send_keys('cerebrinho!')
    send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    send_button.click()
    time.sleep(.5)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path='/home/davi/Downloads/chromedriver_linux64/chromedriver')
driver.get('https://')
name_button = driver.find_element_by_id('your_name')
name_button.send_keys('Test Tester')
time.sleep(2)
email_area = driver.find_element_by_id('your_email')
email_area.send_keys('testtester@gmail.com')
phone_area = driver.find_element_by_id('your_phone')
phone_area.send_keys('999999999')
subject_button = driver.find_element_by_id('your_subject')
subject_button.click()
option_buttons = driver.find_elements_by_tag_name('option')
option_buttons[-1].click()
text_area = driver.find_element_by_id('your_message')
text_area.send_keys('Testando')
send_button = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/div/input')
send_button.click()


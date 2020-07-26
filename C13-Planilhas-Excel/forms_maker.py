from requestium import Session, Keys
import time


password = input("Senha: ")
email = input("Email: ")
session = Session(webdriver_path='/home/davi/Downloads/chromedriver_linux64/chromedriver', browser='chrome')
session.driver.get('http://facebook.com')
email_area = session.driver.find_element_by_id('email')
email_area.send_keys(email)
password_area = session.driver.find_element_by_id('pass')
password_area.send_keys(password)
password_area.submit()
time.sleep(5)
response = session.driver.find_elements_by_tag_name('a')
for link in response:
    print(link.text)

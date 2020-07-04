#! /usr/bin/python3
from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'/home/davi/Downloads/geckodriver')
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name' % (elem.tag_name))
except:
    print('This stupid module was not able to work')

link_element = browser.find_element_by_link_text('More Info')
link_element.click()
link_element01 = browser.find_element_by_link_text('Read Online for Free')
link_element01.click()
#! /usr/bin/python3
from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'/home/davi/Downloads')
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name' % (elem.tag_name))
except:
    print('This stupid module was not able to work')

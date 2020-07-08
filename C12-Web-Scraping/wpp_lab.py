import bs4
import requests
from selenium import webdriver
import pyperclip
import re
import time

msg = pyperclip.paste()
senha_re = re.compile(r'(senha:)(\s)(.*)', re.IGNORECASE)
#mo = senha_re.search(msg)
#print(mo.group(3))


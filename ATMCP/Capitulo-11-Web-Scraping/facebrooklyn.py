#! /usr/bin/python3
import sys
import bs4
import requests
import webbrowser
import time


def get_profile(name, last_name):
    principal_page = requests.get('https://facebook.com/' + name + '.' + last_name)
    bs_principal_page = bs4.BeautifulSoup(principal_page.text, features='html.parser')
    principal_page_links = bs_principal_page.select('img')
    important_photos = len(principal_page_links)
    for i in range(important_photos):
        photo_link = principal_page_links[i].get('src')
        webbrowser.open(photo_link)
        time.sleep(3)


get_profile('caue', 'nakamura')
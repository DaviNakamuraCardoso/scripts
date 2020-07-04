#! /usr/bin/python3
import requests
import bs4
import os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features='html.parser')
comic_element = soup.select('#comic img')
if comic_element == []:
    print('Não conseguimos achar uma imagem cômica')
else:
    comic_url = comic_element[0].get('src')
    res = requests.get('http:' + comic_url)
    res.raise_for_status()
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

previous_link = soup.select('a[rel="prev"]')[0]
url = 'http://xkcd.com' + previous_link.get('href')


#! /usr/bin/python3

#Abre várias páginas com os resultados de uma pesquisa automaticamente a partir de argumentos da linha de comando
import requests, sys, bs4, webbrowser

search = sys.argv[1:]
res = requests.get('https://google.com/search?q=' + ' '.join(search))
#res = requests.get("https://google.com/search?q=jw")
beautiful_links = bs4.BeautifulSoup(res.text, features='html.parser')
links = beautiful_links.select('div#main > div > div > div > a')
num_open = min(5, len(links))
for i in range(num_open):
    webbrowser.open("https://google.com/" + links[i].get('href'))



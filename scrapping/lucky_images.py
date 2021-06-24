#! /home/davi/bin/python3

# lucky_images é um programa que capta diversar imagens de um site
import sys, webbrowser, bs4, requests

#site = sys.argv[1]
#imagem = sys.argv[2:]
site = 'facebook'
n = int(4)
imagem = 'davi+nakamura+cardoso'
pagina = requests.get('https://google.com/search?q=' + site)
bs_pagina = bs4.BeautifulSoup(pagina.text, features='html.parser')
links_principais = bs_pagina.select('div#main > div > div > div > a')[0]
bs_pagina_principal = bs4.BeautifulSoup(requests.get('https://google.com/search?q=' + links_principais.getText() + imagem).text, features='html.parser')
links = bs_pagina_principal.select('div#main > div > div > div > a')
x = min(n, len(links))
for i in range(x):
    bs_paginas = bs4.BeautifulSoup(requests.get('https://google.com/' + links[i].get('href')).text, features='html.parser')
    imagens = bs_paginas.select('img')
    for j in range(len(imagens)):
        webbrowser.open(imagens[j].get('src'))



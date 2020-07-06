#! /usr/bin/python3

#deep_search.py é um programa que abre todas as páginas de produto após pesquisar em sites de compras
import sys
import requests
import bs4
import webbrowser

#Abrindo o site principal
site = sys.argv[1]
n = int(sys.argv[2])
pesquisa_no_site = '+'.join(sys.argv[2:])
pagina = requests.get('https://google.com/search?q=%s' % site)
beatiful_site = bs4.BeautifulSoup(pagina.text, features='html.parser')
link_da_pagina = beatiful_site.select('div#main > div > div > div > a')[0]
pagina_principal = requests.get('https://google.com/search?q=' + link_da_pagina.getText() + 's?k=' + pesquisa_no_site)
resultados = bs4.BeautifulSoup(pagina_principal.text, features='html.parser')
links_dos_resultados = resultados.select('div#main > div > div > div > a')
for i in range(2, n):
    webbrowser.open('https://google.com/' + links_dos_resultados[i].get('href'))


import requests, bs4, webbrowser

arquivo_exemplo = open('exemplo.html')
example_soup = bs4.BeautifulSoup(arquivo_exemplo.read(), features='html.parser')
elementos = example_soup.select('title')
print(elementos[0])
print(elementos[0].getText())
arquivo_exemplo.close()
res = requests.get('https://davinakamuracardoso.github.io/Meu-Primeiro-Site/')
meu_site = bs4.BeautifulSoup(res.text, features='html.parser')
tags = meu_site.select('video')
print(tags)
webbrowser.open('https://davinakamuracardoso.github.io/Meu-Primeiro-Site/')

# ajustes é um programa de ajuste de datas, censura de informações e regularização de textos
import pyperclip
import re
import sys

# Obtendo o texto
texto = pyperclip.paste()

# Definindo uma data:
data_regex = re.compile(r'''
(\d{2})                             # dia      
(-|\.|\s)                           # separador
(\d{2})                             # mês
(-|\.|\s)                           # sepador
(\d{4}|\d{2})                       # ano 
''', re.VERBOSE)

# Definindo uma palavra
endereco_regex = re.compile(r'''Rua
(\s) (\w+) (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? 
(,|-|\s|\.)
(\s)?
(\d{1,5})
(-|,|\.|\s)
(\s)?
(\w+) (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? (\s)? (\w+)? 
(-|\.|,)
''', re.VERBOSE)


def regularizar_datas(separador):
    """
    Essa função regulariza a formatação das datas com base em um separador
    """
    global texto
    novo_texto = data_regex.sub(r'\1' + separador + r'\3' + separador + r'\5', texto)
    pyperclip.copy(novo_texto)


if sys.argv[1] == 'datas':
    regularizar_datas(sys.argv[2])
elif sys.argv[1] == 'censurar':
    pyperclip.copy(endereco_regex.sub('ENDEREÇO CENSURADO', texto))




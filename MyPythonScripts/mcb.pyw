# mcb.pyw Salva e carrega porções de texto no clipboard
# Uso: save <palavra chave> salva o clipboard na palavra chave
# <palavra chave> carrega palavra-chave no clipboard
# list carrega todas as palavras chave no clipboard

import shelve, pyperclip, sys


mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    new_save = pyperclip.paste()
    key = sys.argv[2]
    mcb_shelf[key] = new_save
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'lista':
    pyperclip.copy(str(list(mcb_shelf.keys())))
else:
    key = sys.argv[1]
    pyperclip.copy(mcb_shelf[key])

mcb_shelf.close()

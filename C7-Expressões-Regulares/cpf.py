import re, pyperclip, sys

phone_number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number.search('meu número é 415-555-4242')

texto = pyperclip.paste()
cpf_regex = re.compile(r'\d{9}-\d{2}')
cpfs = cpf_regex.findall(texto)
the_cpfs = '\n'.join(cpfs)
pyperclip.copy(the_cpfs)



import pyperclip, re
phone_regex = re.compile(r'''                                
    ((\d{2})|(\(\d{2}\)))?                                   # código de região
    (-|\.|\s)?                                               # separador
    (\d{5})                                                  # três números intermediários
    (-|\.|\s)                                                # separador
    (\d{4})                                                  # quatro números finais
    (-|\.|\s)?                                               # ponto ou vírgula após o número
    ''', re.VERBOSE)

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+                           # nome do usuário
@                                           # símbolo @
[a-zA-Z0-9.-]+                              # nome do domínio
(\.[a-zA-Z]{2,4}))                          # ponto seguido de outros caracteres
''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[4], groups[6]])
    if groups[1] != '':
        phone_num = '(' + groups[1] + ')' + phone_num
    elif groups[2] != '':
        phone_num = groups[2] + phone_num
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copiado para o clipboard: ')
    print('\n'.join(matches))
else:
    print('Nenhum número de telefone ou email encontrado.')



#estrutura_de_senhas.py é um programa que armazena as senhas de diversos sites e as passa para o clipboard
import sys, pyperclip 

senhas = {'nome': 'Davi Nakamura Cardoso', 'rm': '220763', 'coment': 'Gostei muito da aula e das ferramentas utilizadas.',
          'bye': 'Tchau, gostei muito dessa aula!', 'ano': '3ºA', 'pemail': 'davi.nakamura@p4ed.com', 'gmail': 'davinakamuracardoso@gmail.com'}

if len(sys.argv) < 2:
    print('Usage: python estrutura_de_senhas[conta] - copiar senha da conta')
    sys.exit()

conta = sys.argv[1]

if conta in senhas:
    pyperclip.copy(senhas[conta])
    print(conta, 'copiado para o clipboard.')
else:
    print('Senha não encontrada.')
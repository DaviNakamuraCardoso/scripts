@py.exe C:\Users\Davi\Desktop\MyPythonScripts\pw.py %*
@pause
#estrutura_de_senhas.py é um programa que armazena as senhas de diversos sites e as passa para o clipboard
import sys, pyperclip

pegar_senha(conta)
senhas = {'email': 'F22Raptor123', 'p+': 'F22raptor', 'facebook': 'davi123'}

if len(sys.argv) < 2:
    print('Usage: python estrutura_de_senhas[conta] - copiar senha da conta')
    sys.exit()

conta = sys.argv[1]

if conta in senhas:
    pyperclip.copy()
    print('Senha do', conta, 'copiada para o clipboard.')
else:
    print('Senha não encontrada.')

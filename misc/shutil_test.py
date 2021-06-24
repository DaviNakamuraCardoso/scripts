# O módulo shutil tem funções variadas, como copiar, mover, renomear e apagar arquivos

import shutil, os

# o método copy de shutil copia um arquivo da origem (primeiro argumento), para um destino (segundo arguemento)
abs_doc = os.path.abspath('..\documentos')
shutil.copy('Quiz da Química 1', abs_doc)
# também é possível copiar um arquivo e especificar seu nome:
new_doc = os.path.join(abs_doc, 'QuizdaQuímica2.txt')
shutil.copy('QuizdaQuímica1.txt', new_doc)
# o método copytree copia todos os arquivos de uma pasta para um backup
os.chdir(abs_doc)
dir_name = os.path.dirname(abs_doc)
backup = os.path.join(dir_name, 'MyPyhtonScriptsBackup')
# shutil.copytree('..\MyPythonScripts', backup)
# para mover arquivos e pastas, é possível usar o método move
shutil.move(new_doc, '..')
# o path destino (argumento 2) também pode especificar um arquivo, que renomeará o arquivo a ser movido
quiz2 = os.path.join('..', 'QuizdaQuímica2.txt')
shutil.move(quiz2, 'C:\\Users\\Davi\\Desktop\\MyPythonScripts\\QuizdaQuímica78.txt')
# para apagar arquivos permanentemente, é possível utilizar os métodos:
# os.unlink(path) para apagar um arquivo em um path
# os.rmdir(path) para apagar uma pasta VAZIA
# shutil.rmtree para apagar uma pasta e todos os seus arquivos

# CUIDADO! Antes de usar o método unlink, use print para verificar se está apagando os arquivos corretos
for filename in os.listdir('..\\capitals_quiz'):
    if filename.endswith('.txt'):
        filename = os.path.join('..\\capitals_quiz', filename)
        os.unlink(filename)

# Apagando os arquivos com segurança com o módulo send2trash

import send2trash

bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon não é um vegetal')
bacon_file.close()
send2trash.send2trash('bacon.txt')

# percorrendo arquivos com o método walk do módulo os
for folder_name, subfolders, filenames in os.walk('C:\\Users\\Davi\\Desktop\\Code'):
    print('O folder atual é ' + folder_name)
    for subfolder in subfolders:
        print('Os subfolders são: ' + subfolder)

    for filename in filenames:
        print('Arquivo dentro de ' + folder_name + ': ' + filename)

    print('')

# lendo arquivos zip com  o objeto ZipFile
import zipfile

os.chdir('C:\\Users\\Davi\\Desktop\\')
example_zip = zipfile.ZipFile('example.zip')
example_zip.namelist()
spam_info = example_zip.getinfo('spam.txt')
fileSize = spam_info.file_size
compress = spam_info.compress_size
print('Compressed file is %sx smaller!' % (round(fileSize / compress, 2)))

# extraindo arquivos zip com extract e extractall
example_zip.extract('spam.txt')
# para extrair arquivos zip de diretórios diferentes do atual, basta passar um segundo argumento a extract

# criando arquivos zip e adicionando itens
new_zip = zipfile.ZipFile('newzip.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

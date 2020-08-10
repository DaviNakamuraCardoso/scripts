# renumber realiza uma renumeração de arquivos em uma pasta
import re
import os
import shutil

# definindo uma expressão regular para detectar os arquivos enumerados

numbered_file = re.compile(r'''^(.*?)
(\d{1,3})
(\..*)$
''', re.VERBOSE)


def renumber_file(dir, new_dir):
    """Esta função redefine os números de arquivo em uma pasta, para que não haja lacunas

    :param dir: Nome do diretório em que se deseja fazer a renumeração
    :return: Os arquivos são retornados renomeados, na mesma pasta
    """
    numbered_files = []
    for filename in os.listdir(dir):
        if numbered_file.search(filename):
            numbered_files.append(filename)

    numbered_files.sort()
    a = 1
    new_names = []
    for filename in numbered_files:
        a
        mo = numbered_file.search(filename)
        if len(str(a)) == 1:
            new_filename = mo.group(1) + '00' + str(a) + mo.group(3)
        elif len(str(a)) == 2:
            new_filename = mo.group(1) + '0' + str(a) + mo.group(3)
        else:
            new_filename = mo.group(1) + str(a) + mo.group(3)
        new_names.append(new_filename)
        a += 1
    for filename, new_filename in zip(numbered_files, new_names):
        actual_doc = os.path.join(dir, filename)
        next_doc = os.path.join(new_dir, new_filename)
        shutil.move(actual_doc, next_doc)


renumber_file('..\\documentos', '..\\MyPyhtonScriptsBackup')

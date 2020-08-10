# Cópia seletiva seleciona arquivos jpg e pdf e os copia para uma pasta específica

import os
import shutil
import sys


def copy_arquives(arq1='.pdf', path='MyPythonScriptsBackup', dest='documentos'):
    """Copia o tipo de arquivo inserido de um path para outro

    :param arq1: primeiro tipo de arquivo desejado
    :param path: local do qual se deseja copiar os arquivos
    :param dest: local para onde se deseja copiar os arquivos
    :return: copia dos arquivos para um destino desejado
    """
    path = 'C:\\Users\\Davi\\Desktop\\' + path
    dest = 'C:\\Users\\Davi\\Desktop\\' + dest
    path = os.path.abspath(path)
    os.chdir(path)
    dest = os.path.abspath(dest)
    for folder, subfolder, filenames in os.walk(path):
        folder_name = os.path.basename(folder)
        try:
            os.makedirs('%s\\%s' % (dest, folder_name))
        except FileExistsError:
            continue
        for filename in filenames:
            if filename.endswith(arq1):
                filename = os.path.join(folder, filename)
                dest_ne = os.path.join(dest, folder_name)
                shutil.copy(filename, dest_ne)
        if not len(list(os.listdir(os.path.join(dest, folder_name)))):
            os.rmdir(os.path.join(dest, folder_name))


#copy_arquives('.py', 'Code', 'documentos')


copy_arquives(sys.argv[1], sys.argv[2], sys.argv[3])




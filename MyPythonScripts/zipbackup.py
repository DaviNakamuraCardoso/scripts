# zipbackup copia uma pasta toda e seu conteúdo para um arquivo ZIP cujo nome seja incrementado
import zipfile
import os


def backupzip(folder):
    """Faz backup de todos os arquivos de folder para um zip
    :param folder:
    :return:
    """
    folder = os.path.abspath(folder) # garante que o folder é um path absoluto
    # Determina o nome do arquio de acordo com os arquivos já existentes

    number = 1
    while True:
        zip_filename = 'E:\\Backup\\Backup' + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Cria o arquivo ZIP

    backupzip = zipfile.ZipFile(zip_filename, 'w')

    # Percorre toda a árvore de arquivos e compacta os arquivos da pasta
    for foldername, subfolders, filenames in os.walk(folder):
        #acrescenta a pasta atual ao arquivo ZIP
        backupzip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername, filename))
    backupzip.close()
    print('Pronto!')


backupzip()

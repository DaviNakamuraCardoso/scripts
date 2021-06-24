import os
import csv
from send2trash import send2trash

print('Remover cabeçalhos de arquivos CSV ou deletar cópias?')
command = input('Para deletar, aperte 0; para remover cabeçalhos, 1: ')
new_path = input('Digite o local onde deseja que o programa seja executado: ')


def functions_caller(command='remove headers', new_path='./'):
    """
    :param command: Tells the code what to do.
    :param new_path: Indicates were the copies will be saved
    :return: A function's execution
    """
    os.chdir(new_path)
    os.makedirs('header_removed', exist_ok=True)
    directory = new_path + 'header_removed'
    if command == '0':
        delete_copies(new_path)
    else:
        remove_header(new_path, directory)
    os.chdir('../')


def remove_header(new_path, directory):
    """
    :param new_path: The new path you want to execute
    :param directory: The current directory
    :return: The new CSV files, without a header
    """
    directory_files = os.listdir(new_path)
    for filename in directory_files:
        if filename.endswith('.csv'):
            os.chdir(new_path)
            csv_file = open(filename)
            csv_reader = csv.reader(csv_file)
            csv_data = list(csv_reader)
            os.chdir(directory)
            new_csv_name = filename.strip('.csv') + '_copy.csv'
            new_csv_file = open(new_csv_name, 'w', newline='')
            new_csv_writer = csv.writer(new_csv_file)
            for i in range(1, len(csv_data)):
                new_csv_writer.writerow(csv_data[i])




def delete_copies(directory):
    """
    :param directory: The Directory you want to remove the copies
    :return: The directory without copies
    """
    directory_files = os.listdir(directory)
    for filename in directory_files:
        if filename.endswith('_copy.csv'):
            send2trash(filename)


if __name__ == '__main__':
    functions_caller(command=command, new_path=new_path)

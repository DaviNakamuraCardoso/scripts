import os


def main():
    os.chdir('../down')
    #create_files() 
    delete_files()
    return 


def create_files():
    """
    Generates 10000 files  
    :return: void
    """
    for i in range(10000):
        filename = open('edavi%s' % i, 'a')
        filename.close()
    return


def delete_files():
    """
    Delete all the files from create_files 
    """
    for filename in os.listdir('../down'):
        if filename.startswith('edavi'):
            print('Deletando', filename)
            os.unlink('../down/%s' % filename)
    return 


if __name__ == '__main__':
    main()


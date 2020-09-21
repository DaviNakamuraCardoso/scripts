# Creating visual effects on the terminal with files 

def main():
    generate_files()
    #delete_files

    return 


def generate_files(rows=100, columns=100):
    """
    :param: (int) rows the max number of rows 
    :param: (int) columns the max number of columns
    :return: (void) create multiple files 
    """

    for i in range(rows):
        for j in range(columns):
            filename = open(str(i+j) + '.txt', 'w')
            filename.close()
    return 


if __name__ == '__main__':
    main() 
        

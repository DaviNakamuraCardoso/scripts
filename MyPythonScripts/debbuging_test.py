# para gerar uma exceção, basta digitar a palavra-chave raise e chamar a função Exception(
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')


def box_print(symbol, width, height):
    """
    This function makes a box on the screen based on three parameters:
    :param symbol: a unique symbol
    :param width: 2 or more symbols of widht
    :param height: 2 or more symbols of height
    """
    if len(symbol) > 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Widht must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))


# Obtendo o traceback (mensagen de erro) como uma string
import traceback
try:
    raise Exception('This is the error message.')
except:
    error_file = open('errorfile.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback information was written to errorfile.')

# Asserções são verificações de sanidade do código e contém 4 itens básicos:
# a palavra-chave assert
# uma condição (avaliada como True or False)
# uma vírgula
# uma string de retorno quando a condição for False

factorials = {0: 1, 1: 1}

import sys


sys.setrecursionlimit(500000)


def factorial(i):
    """
    This function defines the factorial result of a parameter based on a recursive method
    :param i: The factorial number that you wish
    :return: The factorial value
    """
    if i not in factorials.keys():
        result = i * factorial(i-1)
        factorials[i] = result
        return result
    else:
        return factorials[i]


def bugged_factorial_example(n):
    """
    This function raises a bugged mechanism to calculate the factorial value of a number n
    :param n: Number that you wish
    :return: The factorial value (n!) of the number n
    """
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ' total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % n)
    return total


print(bugged_factorial_example(5))
print('The 5 factorial is actually ' + str(factorial(10)))
logging.debug('End of program')

# Níveis de logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Alguns detalhes de debugging')
logging.info('O módulo logging está funcionando')
logging.warning('Uma mensagem de erro está prestes a ser exibida')
logging.error('Um erro ocorreu')
logging.critical('O programa não é capaz de recuperar')
# para desabilitar a função debug do módulo logging, basta digitar logging.disable e passar um nível de erro, e todas
# as mensagens abaixo desse nível serão desabilitadas. MAS é necessário posiconar logging.disable antes das chamadas de
# logging

logging.disable(logging.CRITICAL)
logging.error('Erro! Erro!')
logging.info('Info.')
logging.warning('WARNING')
logging.critical('Erro grosseiro!')


# salvando as mensagens de logging em um arquivo
logging.basicConfig(filename='GabaritodoQuiz1.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - '
                                                                                '%(message)s')
# as mensagens de logging em GabaritodoQuiz.txt

# Debugger do IDLE
# O debugger é um programa que permite a execução do programa uma linha de cada vez
first = input('Enter the first number to add: ')
second = input('Enter the second number to add: ')
third = input('Enter the third number to add: ')

print('The sum is ', first + second + third)





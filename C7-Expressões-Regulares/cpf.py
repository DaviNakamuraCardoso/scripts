import re
import pyperclip 
import sys 


def main():

    # Getting the text from the clipboard
    text = pyperclip.paste()
    
    # Getting all the CPFs
    cpfs = get_cpfs(text=text)

    # Finally, the CPFs all copied to the clipboard
    pyperclip.copy('\n'.join(cpfs))

    return 


def get_cpfs(text):
    """
    :param text: The text from which you want to extract the CPF numbers
    :return: A list with all the CPFs in the given text 
    """
    # The Regex to identify the CPF numbers 
    cpf_regex = re.compile(r'\d{3}(.)?\d{3}(.)?\d{3}(-)?\d{2}')

    # Finding all the CPFs 
    cpfs = cpf_regex.findall(text)

    # Returning the texts
    return cpfs  


if __name__ == '__main__':
    main()
     

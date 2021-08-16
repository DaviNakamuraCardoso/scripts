#include <stdio.h>
#include <stdlib.h>
#include "tokens.h"
#include "tokenizer.h"

int main(int argc, const char** argv)
{
    const char* filename = "bible.txt"; 

    if (argc == 2) 
    {
        filename = argv[1];
    }

    DICTIONARY dictionary = new_dictionary(); 
    
    TOKEN** tokens = tokenize(dictionary, filename);

    for (int i = 1; i < tokens[0]; i++) printtoken(tokens[i]);

    return 0; 
}


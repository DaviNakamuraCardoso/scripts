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

    WORD* dictionary = new_dictionary(); 
    
    TOKEN** tokens = tokenize(dictionary, filename);
    return 0; 
}


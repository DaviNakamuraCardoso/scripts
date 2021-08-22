#include <stdio.h>
#include <stdlib.h>
#include <tokens.h>
#include <tokenizer.h>
#include <error.h>

int main(int argc, const char** argv)
{
    FILE* stream = stdin; 

    if (argc == 2) 
    {
        stream = fopen(argv[1], "r"); 
        if (stream == NULL) error("File %s doesn't exist!", argv[1]); 
    }


    DICTIONARY dictionary = new_dictionary(); 
    TOKEN** tokens = tokenize(dictionary, stream);

    for (int i = 1; i < tokens[0]; i++) printtoken(tokens[i]);

    return 0; 
}


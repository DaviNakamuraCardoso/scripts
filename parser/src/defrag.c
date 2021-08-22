#include <stdio.h>
#include <stdlib.h>
#include <tokens.h>

TOKEN** defrag(TOKEN** tokens)
{
    TOKEN** new = calloc(sizeof(TOKEN*), 1000000);

    int i = 1, j = 1; 
    for (; i < tokens[0]; i++, j++)
    {
        if (tokens[j]->type == __UNKNOWN)
        {
            
        }
        

        new[i] = tokens[j]; 
    }

    return new; 

}



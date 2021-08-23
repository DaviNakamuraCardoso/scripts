#include <stdio.h>
#include <stdlib.h>
#include <tokens.h>


static TOKEN* trymerge(TOKEN* first, TOKEN* last)
{

    return NULL;
}

TOKEN** defrag(TOKEN** tokens)
{
    TOKEN** new = calloc(sizeof(TOKEN*), 1000000);

    int i = 1, j = 1; 
    for (; i < tokens[0]; i++, j++)
    {
        if (tokens[j]->type == __UNKNOWN)
        {
            TOKEN* next = trymerge(tokens[i-1], tokens[i]);            
            if (next == NULL)
            {
                next = trymerge(tokens[i], tokens[i+1]);
            }
        }
        

        new[i] = tokens[j]; 
    }

    return new; 

}




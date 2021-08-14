#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "tokenizer.h"


static unsigned int isnewline(char c)
{
    return c == '\n'; 
}

int getword(char* phrase, int index, char* buff)
{
    int i = index;
    int j; 
    for (j = 0; isalnum(phrase[i]) && phrase[i] != '\0'; i++, j++)
    {
        buff[j] = phrase[i]; 
    }
    buff[j] = '\0'; 

    for (; !isalnum(phrase[i]) && phrase[i] != '\0'; i++) {}
    return i-1;

}

int getwords(char* buff)
{
    for (int i = 0; buff[i] != '\0';i++)
    {
        char word[100];
        i = getword(buff, i, word);
        printf("%s\n", word); 

    }
    return 0;
}

// Get the next line 
char* get_line(FILE* f, char* buff)
{
    int i = 0; 
    char c; 
    for (; (c = fgetc(f)) != EOF; i++)
    {
        if (isnewline(c))
        {
            buff[i] = '\0'; 
            return buff; 
        }
        buff[i] = c; 
    }

    buff[i] = '\0'; 
    return NULL; 
} 

    

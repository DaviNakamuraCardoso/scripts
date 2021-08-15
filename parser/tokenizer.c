#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "tokens.h"
#include "tokenizer.h"


TOKEN* new_token(char* word, unsigned int class)
{
    TOKEN* t = malloc(sizeof(TOKEN));
    t->word = strdup(word);
    t->class = class; 

    return t; 
}

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

    for (; isblank(phrase[i]); i++) {}

    if (i == index)
    {
        if (issym(phrase[i])) { buff[0] = phrase[i++]; buff[1] = '\0'; }
        for (; !isalnum(phrase[i]) && phrase[i] != '\0'; i++) {}
    }
    return i-1;

}

TOKEN** tokenize(WORD* dictionary, const char* filename)
{
    FILE* f = fopen(filename, "r");
    TOKEN **tokens = calloc(sizeof(TOKEN*), 10000000);
    char buffer[300];
    unsigned long counter = 0; 

    inline int searchwords(char* buff)
    {
        char debg[300];
        unsigned int type; 
        for (int i = 0; buff[i] != '\0';i++)
        {
            char word[200];
            i = getword(buff, i, word);
            type = search_word(dictionary, word); 
            tokens[counter++] = new_token(word, type); 


            printf("%s => %s\n", word, classtr(type, debg));

        }
        return 0; 
    }

    while (get_line(f, buffer) != NULL)
    {
        searchwords(buffer); 
    }
    return tokens;

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

    

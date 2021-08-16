#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "types.h"
#include "tokens.h"
#include "tokenizer.h"


TOKEN* new_wordt(DICTIONARY d, char* word)
{
    TOKEN* t = malloc(sizeof(TOKEN));
    t->type = __WORD;
    t->word = (WORD*) search_word(d, word); 

    return t; 
}

TOKEN* new_numeralt(DICTIONARY d, char* word)
{
    TOKEN* t = malloc(sizeof(TOKEN));
    t->type = __NUMERAL;
    t->number = atof(word);

    return t; 
}

TOKEN* new_symbolt(DICTIONARY d, char* word)
{
    TOKEN* t = malloc(sizeof(TOKEN));
    t->type = __SYMBOL;
    t->symbol = d.symbols[symboltype(*word)]; 
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
        for (; !isalnum(phrase[i]) && !issym(phrase[i]) && phrase[i] != '\0'; i++){}
    }
    return i-1;

}

TOKEN** tokenize(DICTIONARY dictionary, const char* filename)
{
    FILE* f = fopen(filename, "r");
    TOKEN **tokens = calloc(sizeof(TOKEN*), 10000000);
    char buffer[300];
    unsigned long counter = 1; 


    inline enum tokentype wordtype(char* word)
    {
        if (isnumeral(word)) return __NUMERAL;
        if (issym(*word)) return __SYMBOL;

        return __WORD; 
    }
        
    inline int generatetoken(char* word)
    {
        TOKEN* (*constructors[]) (DICTIONARY, char*) = {
            new_wordt, 
            new_symbolt, 
            new_numeralt 
        };

        tokens[counter++] = constructors[wordtype(word)](dictionary, word);

        return 0;
    }

    inline int searchwords(char* buff)
    {
        for (int i = 0; buff[i] != '\0'; i++)
        {
            char word[200]; 
            i = getword(buff, i, word);
            if (*word == '\0') { i++; continue; } 
            generatetoken(word);     
        }
        return 0; 
    }

    while (get_line(f, buffer) != NULL)
    {
        searchwords(buffer); 
    }
    tokens[0] = counter; 
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

void printtoken(TOKEN* t)
{
    inline void printword(TOKEN* token)
    {
        if (token->word == NULL || token->word->class == INEXISTENT) 
        {
            printf("??? => unknown\n");
            return;
        }
        char buff[200];
        printf("%s => %s\n", token->word->word, classtr(token->word->class, buff)); 
    }

    inline void printsymbol(TOKEN* token)
    {
        printf("%c => %s\n", token->symbol->ascii, token->symbol->str);
    }

    inline void printnumeral(TOKEN* token)
    {
        printf("%f => numeral\n", token->number);
    }


    void (*printers[]) (TOKEN*) = {
        printword,
        printsymbol,
        printnumeral
    };

    printers[t->type](t);
}



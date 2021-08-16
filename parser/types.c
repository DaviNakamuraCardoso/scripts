#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "tokens.h"


enum symbol symboltype(char c)
{
    switch (c) {
        case '!': return EXCLAMATION;
        case '.': return DOT;
        case ',': return COMMA;
        case ':': return COLON;
        case ';': return SEMICOLON; 
        case '?': return QUESTION;
        case '(': return LPARENTHESIS; 
        case ')': return RPARENTHESIS;
    }

    return -1; 
}

unsigned int issym(char c)
{
    switch(c)
    {
        case ',':
        case '.':
        case ':':
        case '?':
        case '!':
        case ';': 
        case '(': 
        case ')': 
            return 1; 
    }
    return 0;
}

unsigned int isnumeral(char* word)
{
    for (int i = 0; word[i] != '\0'; i++)
    {
        if (!isdigit(word[i])) return 0; 
    }
    return 1; 
}

static void cat(char* str, char* lit)
{
    int i; 
    for (i = 0; str[i] != '\0'; i++) {}
    if (i > 0) { str[i++] = ','; }
    for (int j = 0; lit[j] != '\0'; i++, j++) {
        str[i] = lit[j];
    }
    str[i] = '\0'; 
}


char* classtr(unsigned int c, char* str)
{
    char* classes[] = {
        "inexistent", 
        "noun", 
        "verb", 
        "adjective",
        "pronoun",
        "article", 
        "adverb", 
        "conjunction", 
        "preposition", 
        "numeral", 
        "symbol"
    };

    str[0] = '\0';
    for (int i = 0; i < (sizeof classes / sizeof (char*)); i++)
    {
       if ((c >> i & 1))
       {
         cat(str, classes[i]);  
       }
    }
    return str; 

}




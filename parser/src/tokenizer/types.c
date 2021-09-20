#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <types.h>


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
        case '-': return DASH; 
        case 39: return SINGLEQUOTE;
        case '"': return DOUBLEQUOTE;

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
        case '-':
        case 39:
        case '"':
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



unsigned int ischapter(char* word)
{
    int i = 0;
    char* c = NULL; 
    if (isdigit(*word)) i++;
    for (;isalpha(word[i]) && word[i]!='\0';i++) { }
    if (i < 2) return 0; 
    for (c = word+i; *c != '\0'; c++) { if (!isdigit(*c)) return 0; } 
    if (c - word <= i) return 0;  

    return 1; 
}

void printtoken(TOKEN* t)
{
    inline void printword(TOKEN* token)
    {
        if (token->word == NULL || token->word->class == INEXISTENT) 
        {
            printf("??? => unknown word\n");
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
        printf("%.0f => numeral\n", token->number);
    }

    inline void printchapter(TOKEN* token)
    {
        printf("%s => chapter\n", token->content); 
    }

    inline void printunknown(TOKEN* token)
    {
        fprintf(stderr, "%s => UNKNOWN\n", token->content); 
    }

    void (*printers[]) (TOKEN*) = {
        printword,
        printsymbol,
        printnumeral, 
        printchapter, 
        printunknown
    };

    printers[t->type](t);
}


const char* tokenstr(TOKEN* t) 
{
    inline const char* strword(TOKEN* tk) { return tk->word->word; }
    inline const char* strsymbol(TOKEN* tk) { return "S"; }
    inline const char* strnumeral(TOKEN* tk) { return "D";}
    inline const char* strchapter(TOKEN* tk) { return "C"; }
    inline const char* strunknown(TOKEN* tk) { return tk->content; } 

    const char* (*str[]) (TOKEN*) = {
       strword, 
       strsymbol,
       strnumeral,
       strchapter,
       strunknown
    }; 
    
    const char* r = (char*) str[t->type](t);

    return r; 
}

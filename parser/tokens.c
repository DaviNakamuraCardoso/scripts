#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "types.h"
#include "tokens.h"
#include "tokenizer.h"

int ascii(char c)
{ 
    if (!isalpha(c)) return WORDSIZE-1; 
    if (isupper(c)) return c - 'A';
    return c - 'a'; 
}

WORD* new_word(WORD* parent)
{
    WORD* w = malloc(sizeof(WORD));
    for (int i = 0; i < WORDSIZE; i++) w->next[i] = NULL; 
    w->class = INEXISTENT; 
    w->word = NULL; 

    return w; 
}

void add_word(WORD* root, char* word, enum wordclass class)
{
    WORD* current = root; 
    for (int i = 0; word[i] != '\0'; i++)
    {
        int index = ascii(word[i]);
        if (current->next[index] == NULL)
        {
            current->next[index] = new_word(current);
        }
        current = current->next[index];

    }

    // Turns off the "inexistent" bit
    current->class &= ~INEXISTENT;  

    // Turns on the class bit
    current->class |= class;
    current->word = strdup(word); 
}


WORD* search_word(DICTIONARY d, char* word)
{

    if (isnumeral(word) | issym(*word)) return NULL; 

    WORD* current = d.words; 
    for (int i = 0; word[i] != '\0'; i++)
    {
       current = current->next[ascii(word[i])];
       if (current == NULL) return NULL;  
    }

    return current; 

} 


void add_file(WORD* dictionary, const char* filename, enum wordclass class)
{
    char buff[200], word[200];
    FILE *w = fopen(filename, "r");
    while (get_line(w, buff) != NULL)
    {
        getword(buff, 0, word);
        add_word(dictionary, word, class);
    }
    fclose(w); 

    return; 

}

Symbol* new_Symbol(char ascii, enum symbol type, const char* str)
{
    Symbol* s = malloc(sizeof(Symbol));
    s->ascii = ascii; 
    s->type = type;
    s->str = strdup(str);
    return s; 
}



void symbollist(Symbol** emptylist)
{
    emptylist[COMMA] =          new_Symbol(',', COMMA, "comma");
    emptylist[DOT] =            new_Symbol('.', DOT, "dot");
    emptylist[EXCLAMATION] =    new_Symbol('!', EXCLAMATION, "exclamation point");   
    emptylist[COLON] =          new_Symbol(':', COLON, "colon");
    emptylist[SEMICOLON] =      new_Symbol(';', SEMICOLON, "semicolon");
    emptylist[QUESTION] =       new_Symbol('?', QUESTION, "question mark");
    emptylist[LPARENTHESIS] =   new_Symbol('(', LPARENTHESIS, "left parenthesis");
    emptylist[RPARENTHESIS] =   new_Symbol(')', RPARENTHESIS, "right parenthesis");


    return;
}

DICTIONARY new_dictionary(void)
{


    WORD* words = new_word(NULL);
    DICTIONARY d = {.words=words}; 
    symbollist(d.symbols);

    add_file(words, "data/nouns/nouns.txt", NOUN);
    add_file(words, "data/verbs/verbs.txt", VERB); 
    add_file(words, "data/adjectives/adjectives.txt", ADJECTIVE);
    add_file(words, "data/adverbs/adverbs.txt", ADVERB); 
    add_file(words, "data/articles/articles.txt", ARTICLE);
    add_file(words, "data/pronouns/pronouns.txt", PRONOUN);
    add_file(words, "data/conjunctions/conjunctions.txt", CONJUNCTION);
    add_file(words, "data/prepositions/prepositions.txt", PREPOSITION); 

    return d; 
} 

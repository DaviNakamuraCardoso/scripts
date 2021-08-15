#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "tokenizer.h"
#include "tokens.h"

int ascii(char c)
{
    if (!isalpha(c)) return WORDSIZE-1; 
    if (isupper(c)) return c - 'A';

    return c - 'a'; 
}

WORD* new_word(void)
{
    WORD* w = malloc(sizeof(WORD));
    for (int i = 0; i < WORDSIZE; i++) w->next[i] = NULL; 
    w->class = 1; 

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
            current->next[index] = new_word();
        }
        current = current->next[index];

    }

    // Turns off the "inexistent" bit
    current->class &= ~INEXISTENT;  
    // Turns on the class bit
    current->class |= class;

}

unsigned int search_word(WORD* root, char* word)
{
    WORD* current = root; 
    for (int i = 0; word[i] != '\0'; i++)
    {
       current = current->next[ascii(word[i])];
       if (current == NULL) return INEXISTENT;  
    }

    return current->class; 

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


WORD* new_dictionary(void)
{
    WORD* dictionary = new_word();

    add_file(dictionary, "data/nouns/nouns.txt", NOUN);
    add_file(dictionary, "data/verbs/verbs.txt", VERB); 
    add_file(dictionary, "data/adjectives/adjectives.txt", ADJECTIVE);
    add_file(dictionary, "data/adverbs/adverbs.txt", ADVERB); 
    add_file(dictionary, "data/articles/articles.txt", ARTICLE);
    add_file(dictionary, "data/pronouns/pronouns.txt", PRONOUN);
    add_file(dictionary, "data/conjunctions/conjunctions.txt", CONJUNCTION);
    add_file(dictionary, "data/prepositions/prepositions.txt", PREPOSITION); 

    return dictionary; 
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
        "preposition"
    };

    str[0] = '\0';
    for (int i = 0; i < (sizeof classes / sizeof (char*)); i++)
    {
       if ((c >> i & 1))
       {
         cat(str, classes[i]);  
       }
    }
    return; 

}

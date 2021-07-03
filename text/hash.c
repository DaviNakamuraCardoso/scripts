/**
*
*       Implements a Hash Table for the words in a file
*
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <hash.h>


static HASH* new_hash(void)
{
    HASH* h = (HASH*) malloc(sizeof(HASH));
    for (int i = 0; i < HASHSIZE; i++)
    {
        h->words[i] = NULL;
    }

    return h;
}

static WORD* new_word(char* word)
{
    WORD* w = (WORD*) malloc(sizeof(WORD));
    w->next = NULL;
    w->counter = 0;
    w->word = strdup(word);

    return w;
}


/**
*       Hash function from "The C Programming Language", K&R, pg. 61
*
*/
static unsigned long hash(char* word)
{
    unsigned long val = 0, i;
    for (i = 0; word[i] != '\0'; i++)
    {
        val += 31 * word[i];
    }
    return (val % HASHSIZE);
}

static WORD* add_hash(HASH* root, char* word)
{
    unsigned long pos = hash(word);
    WORD* new = new_word(word);

    new->next = root->words[pos];
    root->words[pos] = new;

    return new;
}

static WORD* search_hash(HASH* root, char* word)
{
    WORD* w = root->words[hash(word)];
    for (; w != NULL; w = w->next)
    {
        if (w == NULL) return NULL;
        if (strcmp(word, w->word) == 0) return w;
    }

    return w;
}

static unsigned int isnewline(char c)
{
    return (c == '\n' || c == '\t');
}

static unsigned int get_word(char* buff, unsigned int size, FILE* f)
{
    char c = fgetc(f);
    int count = 0;

    do {
        if (isalnum(c)) buff[count++] = c;
        else if (isnewline(c)) break;

        if ((c = fgetc(f)) == EOF) return 0;

    } while (c != ' ');

    buff[count] = '\0';

    return 1;
}

HASH* mapf(const char* filename)
{
    FILE* f = fopen(filename, "r");
    HASH* root = new_hash();
    WORD* w;
    char buff[46], *newline;

    while (get_word(buff, 46, f))
    {
        if ((w = search_hash(root, buff)) == NULL)
        {
            w = add_hash(root, buff);
        }

        w->counter++;
    }

    return root;
}

unsigned long count(HASH* root, char* word)
{
    WORD* w = search_hash(root, word);

    if (w == NULL) return 0;

    return w->counter;
}

/**
*       Defines a hash
*
*/

#ifndef HASHSIZE
#define HASHSIZE 10001
#endif

typedef struct _word {
    const char* word;
    unsigned long counter;
    struct _word* next;
} WORD;

typedef struct _hash {
    WORD* words[HASHSIZE];
} HASH;

// Constructors
static HASH* new_hash(void);
static WORD* new_word(char* word);

// Utils
static WORD* add_hash(HASH* root, char* word);
static WORD* search_hash(HASH* root, char* word);
static unsigned long hash(char* word);

HASH* mapf(const char* filename);
unsigned long count(HASH* root, char* word);

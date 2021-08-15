

#define WORDSIZE 27

enum wordclass {
    INEXISTENT      =       1,
    NOUN            =       2,
    VERB            =       4,
    ADJECTIVE       =       8,
    PRONOUN         =       16,
    ARTICLE         =       32,
    ADVERB          =       64, 
    CONJUNCTION     =       128, 
    PREPOSITION     =       256, 
    NUMERAL         =       512, 
    SYMBOL          =       1024
};


typedef struct _words {
    struct _words *next[WORDSIZE];
    unsigned int class;
} WORD;

WORD* new_word(void);
void add_word(WORD* root, char* word, enum wordclass class);
void add_file(WORD* dictionary, const char* filename, enum wordclass class);

unsigned int search_word(WORD* root, char* word);
WORD* new_dictionary(void); 

char* classtr(unsigned int c, char *str); 

unsigned int issym(char c); 

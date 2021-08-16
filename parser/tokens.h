

#define WORDSIZE 27 
#define SYMBOLSIZE 10 

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

enum symbol {
    COMMA           ,
    DOT             ,
    EXCLAMATION     ,
    QUESTION        ,
    SEMICOLON       ,
    COLON           , 
    LPARENTHESIS    ,
    RPARENTHESIS    
};  




typedef struct _words {
    struct _words *next[WORDSIZE];
    struct _words *parent;
    unsigned int class;
    char* word; 
} WORD;

typedef struct _symbol {
    enum symbol type; 
    char ascii;
    char* str; 
} Symbol;

typedef struct _dictionary {
    WORD* words;
    Symbol* symbols[SYMBOLSIZE]; 
} DICTIONARY;


WORD* new_word(WORD* parent);
void add_word(WORD* root, char* word, enum wordclass class);
void add_file(WORD* dictionary, const char* filename, enum wordclass class);

WORD* search_word(DICTIONARY d, char* word);
DICTIONARY new_dictionary(void); 

char* classtr(unsigned int c, char *str); 


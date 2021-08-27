

enum tokentype {
    __WORD,
    __SYMBOL,
    __NUMERAL, 
    __CHAPTER, 
    __UNKNOWN 
}; 
        

typedef struct _token {
    unsigned int type:4;
    union {
        char* content; 
        WORD* word;
        Symbol* symbol;
        double number; 
    };


} TOKEN;

char* get_line(FILE* f, char* buff); 
int getwords(char* buff); 
int getword(char* phrase, int index, char* buff); 
TOKEN** tokenize(DICTIONARY dictionary, FILE* stream);  



enum tokentype {
    __WORD,
    __SYMBOL,
    __NUMERAL, 
    __CHAPTER
}; 
        

typedef struct _token {
    unsigned int type:2;
    union {
        WORD* word;
        Symbol* symbol;
        double number; 
        char* content; 
    };


} TOKEN;

char* get_line(FILE* f, char* buff); 
int getwords(char* buff); 
int getword(char* phrase, int index, char* buff); 
TOKEN** tokenize(DICTIONARY dictionary, const char* filename);  
void printtoken(TOKEN* t); 

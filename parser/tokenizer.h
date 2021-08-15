

typedef struct _token {
    char* word;
    unsigned int class; 
} TOKEN;

char* get_line(FILE* f, char* buff); 
int getwords(char* buff); 
int getword(char* phrase, int index, char* buff); 
TOKEN** tokenize(WORD* dictionary, const char* filename);  

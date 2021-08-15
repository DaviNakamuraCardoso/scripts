

typedef struct _word {
    char* word;
} word;

char* get_line(FILE* f, char* buff); 
int getwords(char* buff); 
int getword(char* phrase, int index, char* buff); 

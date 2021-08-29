
typedef struct _list List; 
List* new_list(void);
void addl(List* l, void* t);
void* getelement(List* l, unsigned long index);
unsigned long listlength(List* l); 

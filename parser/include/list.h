
typedef struct _list List; 
List* new_list(void);
void addl(List* l, void* t);
void* getelement(List* l, unsigned long index);
const void* popl(List* l); 
unsigned long listlength(List* l); 


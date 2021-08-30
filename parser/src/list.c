#include <stdio.h>
#include <stdlib.h>
#include <tokens.h>
#include <tokenizer.h>
#include <list.h>

typedef struct _list {
    TOKEN** contents;
    unsigned long elems;
    unsigned short maxsizei;
} List; 



static int LIST_SIZES[] = {
    10, 
    100, 
    1000, 
    10000, 
    100000, 
    1000000, 
    10000000,
    100000000
}; 

List* new_list(void)
{
    List *l = malloc(sizeof(List));
    l->contents = calloc(sizeof(TOKEN*), LIST_SIZES[0]); 
    l->maxsizei = 0; 
    l->elems = 0; 

    return l; 

}
void increasel(List* l)
{
    
    l->contents = reallocarray(
            l->contents, 
            LIST_SIZES[++l->maxsizei], 
            sizeof(TOKEN*)
            );
    return;
}


void addl(List* l, void* t)
{
    inline unsigned int atmaxsize(List* l)
    {
        return l->elems == LIST_SIZES[l->maxsizei]-1;
    }

    if (atmaxsize(l)) increasel(l);

    l->contents[l->elems++] = (TOKEN*) t;

    return;
}


unsigned long listlength(List* l)
{
    return l->elems;
}

void* getelement(List* l, unsigned long index)
{
    return l->contents[index];
}

const void* popl(List* l)
{
    if (l->elems == 0){ return NULL;}
    return (TOKEN*) l->contents[--(l->elems)];
}


void testlist(void)
{
    List* l = new_list();
    for (int i = 0; i < 10100; i++) addl(l, NULL); 

    for (int i = 0; i < listlength(l); i++) 
    {
        printf("%i element is NULL\n", i);
        if (l->contents[i] != NULL) break;
    }

   return;
}




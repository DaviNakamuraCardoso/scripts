#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <types.h>
#include <list.h>


static TOKEN* build_word(WORD* w)
{
    TOKEN* t = malloc(sizeof(TOKEN));
    t->type = __WORD;
    t->word = (WORD*)  w;

    return t; 
}

inline static unsigned int iscapitalized(char* word)
{
    return isupper(*word);
}

static TOKEN* nounh(TOKEN* t)
{
    WORD* w = malloc(sizeof(WORD));
    t->type = __WORD;
    w->word = strdup(t->content);
    w->class = NOUN;
    t->word = w;
    return t;
}

static TOKEN* mergetokens(Dictionary d, TOKEN* first, TOKEN* last)
{
    WORD *w;
    char buff[300];

    strcpy(buff, tokenstr(first));
    strcat(buff, tokenstr(last));
    printf("Trying %s\n", buff);

    w = search_word(d, buff);
    
    if (w == NULL || w->class == INEXISTENT) return NULL;


    return build_word(w);
    
}

void addt(Dictionary d, List* l, TOKEN* new)
{

    inline unsigned int canmerge(TOKEN* tk)
    {
        return tk->type == __WORD || tk->type == __UNKNOWN;
    }

    TOKEN* previous = (TOKEN*) popl(l), *t;

    if (previous == NULL) 
    {
        addl(l, new);
        return;
    }

    if (!canmerge(new) || !canmerge(previous)) goto end;

    if (previous->type == __UNKNOWN)
    {
        t = mergetokens(d, previous, new);

        if (t == NULL)
        {
            if (iscapitalized(previous->content))
                previous = nounh(previous);
            goto end; 
        }

        addl(l, t);
        return;
    }

    if (new->type == __UNKNOWN)
    {
        t = mergetokens(d, previous, new);
        if (t == NULL) 
        {
            if (iscapitalized(new->content))
                new = nounh(new);

            goto end; 
        }
        addl(l, t);
        return;
    }

end:
   
    addl(l, previous);
    addl(l, new);

    return; 

}




#include <stdio.h>
#include <stdlib.h>
#include "tokenizer.h"
#include "tokens.h"

void parse(WORD* dictionary); 

int main(void)
{
    WORD* dictionary = new_dictionary(); 
    
    parse(dictionary);
    return 0; 
}

void parse(WORD* dictionary)
{
    FILE *f = fopen("bible.txt", "r");
    char buffer[300];

    inline int searchwords(char* buff)
    {
        for (int i = 0; buff[i] != '\0';i++)
        {
            char word[100], type[200];
            
            i = getword(buff, i, word);
            classtr(search_word(dictionary, word), type); 
            printf("%s => %s\n", word, type); 
        }
        return 0;
    }


    while (get_line(f, buffer) != NULL)
    {
        searchwords(buffer);
    }

}

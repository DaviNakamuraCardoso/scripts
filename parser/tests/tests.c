#include <stdio.h>
#include <stdlib.h>

int test_getline(void); 

int main(void)
{

    unsigned int (*tests[]) (void) = {
        test_getline, 
    };

    for (int i = 0; i < 1; i++)
    {
        if (tests[i]())
        {
            printf("Error in test %i\n", i);
        }
    }
    return 0; 
}


int cmpfile(const char* path)
{
    char out[200], cmp[200]; 
    FILE *outf, *cmpf;
    char o, c; 

    sprintf(out, "%s.out", path);
    sprintf(cmp, "%s.cmp", path);

    outf = fopen(out, "r"); cmpf = fopen(cmp, "r");
    
    for (; (o = fgetc(outf)) != EOF && (c = fgetc(cmpf)) != EOF; )
    {
        if (o != c) return 1; 
    }

    return 0;
}

int test_getline(void)
{
    char buff[200];
    char* cmp = "testfiles/tokenizer/getline/tokenizer.cmp"; 
    FILE* f = fopen("testfiles/tokenizer/getline/tokenizer.in", "r");
    FILE* out = fopen("testfiles/tokenizer/getline/tokenizer.out", "w");
    for (; get_line(f, buff) != NULL; i++)
    {

        fprintf(out, "%s\n", buff);
    }

    fclose(f); fclose(out); 

    return cmpfile("tokenizer/getline/tokenizer");

}


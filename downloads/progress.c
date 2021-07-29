/*
 *      Progress bar
 */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define SIZE 10
#define FILL "#"

void bar(int n);

int main(void)
{
    printf("Progress bar\n");
    
    for (int i = 0; i < 10; i++)
    {
        bar(i);
        usleep(100000);
    }

    printf("\nEnd\n");
    return 0;

}


void bar(int n)
{
    printf("\r[");

    for (int i = 0; i < n; i++)
    {
        printf(FILL);
    }

    for (int i = 0; i < SIZE - n - 1; i++)
    {
        printf(" ");
    }

    printf("]");

    fflush(stdout);
    
    return;
}




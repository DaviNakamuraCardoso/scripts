#include <stdio.h>

int main(void)
{
    char name[300];
    printf("What is your name? ");
    fgets(name, 300, stdin);
    printf("Hello, %s", name);
    return 0;
}

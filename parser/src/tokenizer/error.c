#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>


void error(const char* msg, ...)
{
    int j = 0, i;
    char buff[300]; 
    va_list args;  

    va_start(args, msg);


    buff[0] = '\0'; 

    for (i = 0; msg[j] != '\0'; i++, j++)
    {
        if (msg[j] == '%') 
        {
            switch(msg[++j])
            {
                case 'i': 
                {
                   int val = va_arg(args, int); 
                   sprintf(buff, "%s%i", buff, val); 
                   for (; val > 9; val /= 10, i++) {}
                   break; 
                }
                case 's': 
                {

                    char* str = va_arg(args, char*); 
                    strcat(buff, str); 
                    i += strlen(str)-1; 
                    break; 
                }
                case 'c': 
                {
                    char c = (char) va_arg(args, int); 
                    sprintf(buff, "%s%c", buff, c);
                    break;
                }

                default: 
                {
                    error("Invalid string format"); 
                }
            }
            continue; 
        }

        buff[i] = msg[j];  

    }

    buff[i] = '\n'; 
    buff[++i] = '\0'; 

    fprintf(stderr, buff); 

    va_end(args); 

    exit(1); 
}

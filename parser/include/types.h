
#ifndef _TOKENSH
#define _TOKENSH
#include <tokens.h>
#include <tokenizer.h>
#endif

unsigned int issym(char c); 
unsigned int isnumeral(char* word); 
unsigned int ischapter(char* word); 
char* classtr(unsigned int c, char* str); 
enum symbol symboltype(char c);
void printtoken(TOKEN* t);  


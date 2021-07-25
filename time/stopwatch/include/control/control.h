/**
 * 
 *
 *
 */

#include <stdio.h>
#include <time.h>

#include <control/control.h>


typedef long double ld; 

TIMER* start(void)
{
    TIMER *t = (TIMER*) malloc(sizeof(TIMER));

    t->current = 0; 
    t->previous = 0;

    return t;
}


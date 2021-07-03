/**
*
*       Find the occurencies of a ward in Bible (KJV)
*/

#include <stdio.h>
#include <hash.h>

int main(int argc, char** argv)
{
    if (argc != 2) return 1;
    HASH* map = mapf("bible.txt");

    printf("The word %s appears %li times in the Bible\n", argv[1], count(map, argv[1]));

    return 0;
}

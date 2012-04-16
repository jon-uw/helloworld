#include <stdio.h>
#include <stdlib.h>

#define MEM_BLOCK 8 * 1024 * 1024

//WARN:justfor a test
//we should free malloced memory after using it
static void print_heap_limit() 
{
    int count = 0;
    while (malloc(MEM_BLOCK))
        count++;
    printf("max heap size we can malloc is: %dM\n", count * 8);
}

//realloc allocates another area that is large enough,
//copies the existing data to the new area, [[frees the old area, 
//and returns the pointer to the new area

//if the first argments of realloc is NULL point, then it acts like malloc
static void realloc_test() 
{
    int *p = malloc(MEM_BLOCK);
    int *q = NULL;
    printf("malloced address is: %012p\n", p);
    q = p;
    p = realloc(p, 20 * MEM_BLOCK);
    if (!p) {
        printf("error realloc p\n");
    } else {
        printf("realloced address is: %012p\n", p);
    }
    free(p);
}

int main(int argc, char *argv[])
{
    //print_heap_limit();
    realloc_test();
    getchar();
    return 0;
}

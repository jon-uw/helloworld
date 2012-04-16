#include <stdio.h>
#include <stdlib.h>

const char *CONSTANT_EXAMPLE = "constant example";
int global_int = 15;
long sum[1000];

static void print_address(const char *mem_type, void *ptr) 
{
    printf("%s => %p\n", mem_type, ptr);    
}
/**
 * thanks to: http://blog.ooz.ie/2008/09/0x03-notes-on-assembly-memory-from.html
 * http://en.wikipedia.org/wiki/Data_segment
 * high adress => low
 * stack => heap => bss(uninitialized data) => initialized data => text(code)
 */
int main(int argc, char *argv[]) 
{
    int a = 15;
    int *p = (int *)malloc(sizeof(int));
    print_address("const", (void *)CONSTANT_EXAMPLE);
    print_address("data.global",&global_int);
    print_address("bss.sum",sum);
    print_address("stack", &a);
    print_address("heap", p);
    print_address("text.code", &main);
    getchar();
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

// exit(clean resource) & _Exit(just return) from <stdlib.h> 
// _exit from <unistd.h>, defined in posix  standard
int main(int argc, char *argv[])
{
    int count = printf("test the exit function\n");
    printf("print %d characters:\n", count);
//    exit(245);
}

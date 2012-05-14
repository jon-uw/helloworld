#include <stdio.h>
#include <stdlib.h>

// exit(clean resource) & _Exit(just return) from <stdlib.h> 
// _exit from <unistd.h>, defined in posix  standard
// _Exit is the same as _exit except it's defined in the ISO 
// eventually, exit calls _exit or _Exit to return
int main(int argc, char *argv[])
{
    int count = printf("test the exit function\n");
    printf("print %d characters:\n", count); 
    // here, gcc will return the count of words printf sending to terminal
//    exit(245);
}

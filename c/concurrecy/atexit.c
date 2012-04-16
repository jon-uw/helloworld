#include <stdio.h>
#include <unistd.h>

static void my_exit1(void);
static void my_exit2(void);

/**
  the 'exit' function calls exit handlers in reverse order of their registration
*/
int main(int argc, char *argv[])
{
    atexit(my_exit2);
    atexit(my_exit1);
    atexit(my_exit1);
    printf("Main is done.\n");
//    _Exit(-1); // this will not call the exit handlers
    return 0;
}

static void my_exit1(void)
{
    printf("first exit handler\n");
}

static void my_exit2(void)
{
    printf("the second exit handler\n");
}

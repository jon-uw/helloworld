#include <stdio.h>
#include <unistd.h>

extern char **environ;

int main(int argc ,char *argv[])
{
    //char *p = NULL;
    //while ((p = *(environ++)) != NULL)
    //    printf("%s\n", p);

    if (argc >=2 ) {
        printf("%s => %s\n", argv[1], getenv(argv[1]));
        _exit(0);
    }

    // from gnu coreutils
    while (*environ)
        puts(*environ++);

    return 0;
}

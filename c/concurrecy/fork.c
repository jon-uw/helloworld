#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    pid_t pid = fork();
    if (pid == 0) {
        printf("in child: %d\n", getpid());
        sleep(50 * 1000);
    } else {
        printf("in parent: %d\n", getpid());
        sleep(50 * 1000);
    }

    return 0;
}

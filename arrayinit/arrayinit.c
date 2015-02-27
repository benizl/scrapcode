
#include <stdio.h>
#include <stdint.h>

char a[] = {0, 1};
char *b;

typedef struct fus {
    uint8_t *elem;
} fu_t;

int main(int argc, char** argv)
{
    uint8_t c = 0;

    fu_t bar = {
        .elem = &c,
    };

    return 0;
}


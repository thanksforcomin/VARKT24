#include <stdio.h>

typedef struct
{
    double d;
    int i;
} a;

int main()
{
    printf("%zu", sizeof(a));
}
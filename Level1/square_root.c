#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long n) {
    long long answer = 0;
    long long i = 0;
    if (n == 1)
        return (long long)4;
    while (i < n)
    {
        if ((i * i) == n)
            return ((i + 1) * (i + 1));
        i++;
    }
    return (long long)(-1);
}

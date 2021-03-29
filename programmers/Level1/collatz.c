#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num) {
    int count = 0;
    long long n = (long long)num;
    if (num == 1)
        return 0;
    while (count++ < 500)
    {
        n = (n % 2 == 0) ? n / 2 : n * 3 + 1;
        if (n == 1)
            return (count);
    }
    return -1;
}

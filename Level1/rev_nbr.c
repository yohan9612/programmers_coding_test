#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int numlen(long long n)
{
    int len = 0;
    while (n / (long long)10 != 0)
    {
        len++;
        n /= (long long)10;
    }
    len++;
    return (len);
}

int* solution(long long n) {
    int len = numlen(n);
    int i = 0;
    int* answer = (int*)malloc(sizeof(int) * (len));
    while (i < len)
    {
        answer[i] = n % (long long)10;
        if (n >= (long long)10)
            n /= (long long)10;
        i++;
    }
    return answer;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int sum_digit(int n)
{
    int sum = 0;
    int i = 0;
    if (n >= 10)
    {
        sum = sum_digit(n / 10);
    }
    sum += n % 10;
    return (sum);
}

int solution(int n) {
    int answer = 0;
    answer= sum_digit(n);
    return answer;
}

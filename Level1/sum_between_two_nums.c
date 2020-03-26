#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long ft_sum(int a, int b)
{
    long long i;
    long long sum;
    long long tmp_a;
    long long tmp_b;
    
    i = 0;
    sum = 0;
    tmp_a = (long long)a;
    tmp_b = (long long)b;
    while (i < tmp_b - tmp_a + (long long)1)
    {
        sum += tmp_a;
        tmp_a++;
    }
    return sum;
}

long long solution(int a, int b)
{
    long long answer;
    
    answer = 0;
    if (a == b)
        answer = (long long)a;
    else if (b > a)
        answer = ft_sum(a, b);
    else if (a > b)
        answer = ft_sum(b, a);
    return answer;
}

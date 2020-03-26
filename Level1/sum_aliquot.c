#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int find_divide(int n)
{
    int i;
    int sum;
    
    i = 1;
    sum = 0;
    while (i <= n)
    {
        if (n % i == 0)
            sum += i;
        i++;
    }
    return (sum);
}

int solution(int n) {
    int answer = 0;
    answer = find_divide(n);
    return answer;
}

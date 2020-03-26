#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int s = 0;
    int temp = x;
    s += temp % 10;
    while (temp / 10 != 0)
    {
        temp /= 10;
        s += temp % 10;
    }
    printf("%d", s);
    if (x % s != 0)
        answer = false;
    return answer;
}

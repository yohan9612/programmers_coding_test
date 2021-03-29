#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int n) {
    char* answer = (char*)malloc(sizeof(char) * (n * 3 + 1));
    char* watermellon = (char *)malloc(sizeof(char) * (6));
    
    watermellon = "수박";

    int i = 0;
    
    while (i < n * 3)
    {
        answer[i] = watermellon[i % 6];
        i++;
    }
    answer[i] = '\0';
    return answer;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    char** dates = (char**)malloc(sizeof(char*) * 7);
    int* months = (int*)malloc(sizeof(int) * 12);
    int days = 0;
    months[0] = 31;
    months[1] = 29;
    months[2] = 31;
    months[3] = 30;
    months[4] = 31;
    months[5] = 30;
    months[6] = 31;
    months[7] = 31;
    months[8] = 30;
    months[9] = 31;
    months[10] = 30;
    months[11] = 31;
    int i = 0;
    while (i < 7)
    {
        dates[i] = (char *)malloc(sizeof(char) * 4);
        i++;
    }
    dates[0] = "FRI";
    dates[1] = "SAT";
    dates[2] = "SUN";
    dates[3] = "MON";
    dates[4] = "TUE";
    dates[5] = "WED";
    dates[6] = "THU";
    
    i = 0;
    while (i < a - 1)
    {
        days += months[i];
        i++;
    }
    days += b - 1;
    return dates[days % 7];
}

#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    int i = 0;
    int j;
    while (i < b)
    {
        j = 0;
        while (j < a)
        {
            printf("*");
            j++;
        }
        printf("\n");
        i++;
    }
    return 0;
}

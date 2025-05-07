//
// Created by 강준영 on 25. 3. 21.
//
#include <stdio.h>
int main(void){
    int n,i,j,k;
    printf("몇 단 삼각형입니까?: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n-i; j++)
        {
            printf(" ");
        }
        for (k = 0; k < i * 2 + 1; k++)
        {
            printf("*");
        }
        printf("\n");
    }
}
//
// Created by 강준영 on 25. 3. 21.
//
#include <stdio.h>
int main(void){
    int n,i,j,k;
    printf("몇 단 삼각형입니까?: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i+=2)
    {
        for (j = 0; j < (n-i)/2; j++)
        {
            printf(" ");
        }
        for (k = 0; k < i; k++)
        {
            printf("*");
        }
        printf("\n");
    }
}
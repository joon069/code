//
// Created by 강준영 on 25. 3. 21.
//
#include <stdio.h>
int main(void){
    int n;
    printf("몇 단 삼각형입니까?: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++) {
            printf(" ");
        }
        for (int k = 0; k < (i-1)*2+1; k++) {
            printf("*");
        }
        printf("\n");
    }
}
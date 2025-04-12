#include<stdio.h>
int main(void)
{
    int n;
    scanf("%d", &n);
    for(int i=0; i<n;i++){
        for(int j=n-1; j>i; j--){
            printf(" ");
        }
        for(int ii=0; ii<=i; ii++){
            printf("*");
        }
        printf("\n");
    }
}
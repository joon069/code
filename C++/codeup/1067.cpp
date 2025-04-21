#include <stdio.h>
int main(void)
{
    int num;
    scanf("%d", &num);
    if(num>0){
        if(num%2==0){
            printf("plus\neven");
        }
        else printf("plus\nodd");
    }
    else{
        if(num%2==0){
            printf("minus\neven");
        }
        else printf("minus\nodd");
    }
}

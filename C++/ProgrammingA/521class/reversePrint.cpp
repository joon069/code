#include <stdio.h>
int main(void)
{
    int seven[7];
    for(int i=0; i<7; i++){
        scanf("%d", &seven[i]);
    }
    for(int i=6; i>=0; i--){
        printf("%d ", seven[i]);
    }
    return 0;
}
#include <stdio.h>

int main()
{
    int a[9];
    for(int i= 0; i<9; i++){
        scanf("%d", &a[i]);
    }
    int max = 0;
    int max_idx = 0;
    for(int i=0; i<9;i++){
        if(a[i]>max){
            max = a[i];
            max_idx = i;
        }
    }
    printf("%d\n", max);
    printf("%d", max_idx+1);

    return 0;
}
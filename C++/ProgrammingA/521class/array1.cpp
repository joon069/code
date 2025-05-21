#include <stdio.h>

int main(void)
{
    int arr[5];
    for(int i = 0; i<5; i++){
        scanf("%d", &arr[i]);
    }
    //출력
    for(int i =0; i<5; i++){
        printf("%d", arr[i]);
    }
    //합
    int sum = 0;
    for(int i=0; i<5;i++){
        sum += arr[i];
    }
    printf("%d", sum);
    return 0;
}
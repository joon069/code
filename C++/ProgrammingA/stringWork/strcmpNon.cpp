#include <stdio.h>

int main(void)
{
    char a[100], b[100];
    scanf("%s %s", a, b);
    int s=0;
    for (int i = 0; i < 100; i++){
        if(a[i] != b[i]){
            s = a[i] - b[i];
            break;
        }
    }
    printf("%d", s);
    return 0;
}
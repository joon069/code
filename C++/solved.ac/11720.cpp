#include <stdio.h>

int main(void)
{
    char str[101];
    int n;
    scanf("%d", &n);
    
    scanf("%s", str);
        
    int sum=0;
    
    for(int i=0; str[i]!='\0'; i++){
        sum += str[i] - '0';
    }
    printf("%d", sum);
    
    return 0;
}
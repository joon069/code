#include <stdio.h>
int main()
{
    char a[100];
    int i, len=0;
    int TrueFalse = 1;
    scanf("%s", a);
    
    while(a[len]!='\0'){
        len++;
    }
    
    for(i=0; i < len/2; i++){
        if(a[i] != a[len-1-i]){
            TrueFalse = 0;
            break;
        }
    }
    printf("%d", TrueFalse);
    
    return 0;
}
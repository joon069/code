#include <stdio.h>
int main(void)
{
    char str[101];
    char result[101];
    int i =0, j = 0;
    scanf("%[^\n]s", str);
    while(str[i]!='\0'){
        if(str[i] != 32){
            result[j++] = str[i];
        }
        i++;
    }
    result[j] = '\0';
    printf("%s", result);
}
#include <stdio.h>
#include <string.h>

int main(void)
{
    int az[26], i;
    char str[1001];
    scanf("%s", str);
    for(int i =0; i<26; i++){
        az[i] = -1;
    }
    for(i=0;str[i]!='\0';i++){
        if(az[str[i]-'a'] == -1){
            az[str[i]-'a'] = i;
        }
    }
    for(i=0; i<26; i++){
        printf("%d ", az[i]);
    }
    return 0;
}
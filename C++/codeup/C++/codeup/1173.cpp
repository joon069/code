#include <stdio.h>

int main(void)
{
    int h, m;
    scanf("%d %d", &h, &m);
    
    if(m-30 < 0){
        h -= 1;
        m += 30;
        if(h < 0){
            printf("%d %d", 23, m);
        }
        else printf("%d %d", h, m);
    }
    else printf("%d %d", h, m-30);
    
    return 0;
}
#include <stdio.h>

int main()
{
    int score;
    scanf("%d", &score);
    
    if(90<= score && score <= 100)
    {
        printf("A");
    }
    else if(70<= score && score <= 89)
    {
        printf("B");
    }
    else if(40<= score && score <= 69)
    {
        printf("C");
    }
    else if(0<=score && score <= 39)
    {
        printf("D");
    }
    return 0;
}
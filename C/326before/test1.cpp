#include <stdio.h>

int main()
{
    int up = 0, down = 0, days = 0, oneDay = 0, goal =0;

    scanf("%d %d %d", &up, &down, &goal);
            //2 1 5
    oneDay = up - down;
    
    while(1) {
        
       if(goal - oneDay > 0){
            days++;
       }
       else{
           printf("%d", days);
           break;
       }
    }
    
    
    return 0;

}
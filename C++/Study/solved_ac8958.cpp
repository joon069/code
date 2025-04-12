#include<stdio.h>
#include<string.h>
int main(void)
{
    int n, sum=0, y=0;
    char q[80] ="";
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        scanf("%s", q);
        sum =0;
        y=0;
        for(int j =0; j<strlen(q); j++){
            if(q[j]=='O'){
                y++;
                if(q[j-1]=='X'){
                    y=1;
                    sum += y;
                }
                else{
                    sum +=y;
                }
            }
        }
        printf("%d", sum);
        printf("\n");
    }
    return 0;
}
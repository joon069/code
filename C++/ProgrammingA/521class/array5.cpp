#include <stdio.h>
int main(void)
{
  int seven2[7];
    for(int i=0; i<7; i++){
        scanf("%d", &seven2[i]);
    }
    int front =0, back=6;
    for(int i=0; i<7/2; i++){
        seven2[front] = seven2[front] ^ seven2[back];
        seven2[back] = seven2[front] ^ seven2[back];
        seven2[front] = seven2[front] ^ seven2[back];
        
        front += 1;
        back -= 1;
    }
    for(int i=0; i<7; i++){
        printf("%d ", seven2[i]);
    }
  return 0;
}
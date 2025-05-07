#include <stdio.h>
int main(void)
{
    int a, b, total1=0, total2=0, back=0, real=0;
    scanf("%d %d", &a, &b);
    
    if(a/1000==1){
        total1 += 8;
        a-=1000;
    }
    
    if(a/100==1){
        total1 += 4;
        a-=100;
    }
    
    if(a/10==1){
        total1 += 2;
        a-=10;
    }
    
    if(a/1==1){
        total1 += 1;
        a-=1;
    }
    
    //선
    
    if(b/1000==1){
        total2 += 8;
        b-=1000;
    }
    
    if(b/100==1){
        total2 += 4;
        b-=100;
    }
    
    if(b/10==1){
        total2 += 2;
        b-=10;
    }
    
    if(b/1==1){
        total2 += 1;
        b-=1;
    }
    printf("%d\n", total1);
    printf("%d\n", total2);
    
    
    back = total1 + total2;
    if(back/16==1){
        back-=16;
        real+=10000;
    }
    if(back/8==1){
        back-=8;
        real+=1000;
    }
    if(back/4==1){
        back-=4;
        real+=100;
    }
    if(back/2==1){
        back-=2;
        real+=10;
    }
    if(back/1==1){
        back-=1;
        real+=1;
    }
    
    printf("%d", real);
    
}
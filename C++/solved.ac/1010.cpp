#include <stdio.h>
long long nPr(int n, int r){
    long long sum=1;
    if(r > (n-r)) r = n-r;
    for(int i=1; i<=r; i++){
        sum = sum * (n-i+1)/i;
    }
    return sum;
}
int main()
{
    int t, n, r;
    scanf("%d", &t);
    for(int i=0;i<t;i++){
        scanf("%d %d", &r, &n);
        printf("%lld\n", nPr(n,r));
    }

    return 0;
}
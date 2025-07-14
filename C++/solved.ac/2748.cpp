#include <stdio.h>
long long arr[90] = {0, 1, };
long long fibo(int n){
    if(n < 2) return n;
    else if(arr[n] != 0) return arr[n];
    else {
        arr[n] = fibo(n-1) + fibo(n-2);
        return arr[n];
    }
}

int main(void)
{
    int n;
    scanf("%d", &n);
    printf("%lld", fibo(n));
}
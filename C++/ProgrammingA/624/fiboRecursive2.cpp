#include <stdio.h>
int fibo(int a){
  if (a == 0)
    return 0;
  if (a == 1)
    return 1;
  return fibo(a - 1) + fibo(a - 2);
}
int main(void){
  int a;
  scanf("%d", &a);
  printf("%d", fibo(a));

  return 0;
}
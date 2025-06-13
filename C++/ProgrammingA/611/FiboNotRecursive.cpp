#include <stdio.h>

int fibo(int n){
  int a = 0, b = 1, c;
  for (int i = 2; i <= n; i++){
    c = a + b;
    a = b;
    b = c;
  }
  return b;
}
int main(void){
  int n;
  scanf("%d", &n);
  printf("%d", fibo(n));

  return 0;
}
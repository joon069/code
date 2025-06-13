#include <stdio.h>
int prime(int n){
  for (int i = 2; i <= n / 2; i++){
    if(n % i == 0){
      return 0;
    }
  }
  return 1;
}
int main(void)
{
  int n;
  scanf("%d", &n);
  printf("%d", prime(n));
  return 0;
}
#include <stdio.h>
int fac(int n)
{
  int i, sum = n;
  for (i = n-1; i >= 1; i--){
    sum *= i;
  }
  return sum;
}
int main(void)
{
  int n;
  scanf("%d", &n);
  printf("%d", fac(n));

  return 0;
}
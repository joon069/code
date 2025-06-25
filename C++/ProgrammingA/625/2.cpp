#include <stdio.h>
int c = 0;
int solve(int n)
{
  c += 1;
  if (n <= 1)
    return 1;
  if(n%2 == 0) return solve(n - 1) + solve(n - 2);
  return solve(n - 1);
}
int main(void){
  printf("%d\n", solve(5));
  printf("%d", c);
  return 0;
}
#include <stdio.h>
int c = 0;
int mult(int n)
{
  c+=1;
  if(n == 1) return 2;
  return 2 * mult(n - 1);
}
int main(void)
{
  printf("%d\n", mult(4));
  printf("%d", c);
  return 0;
}
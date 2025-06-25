#include <stdio.h>
int c;
void b(int n)
{
  c++;
  if (n == 0)
    return;
  b(n / 2);
  printf("%d", n % 2);
}
int main(void)
{
  int n;
  scanf("%d", &n);
  b(n);
  printf("%d", c);
  printf("\n");
  return 0;
}
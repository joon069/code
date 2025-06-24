#include <stdio.h>
int main(void)
{
  int n, m=1;
  int place = 1;
  scanf("%d", &n);
  if(n == 0) printf("%d이다.", n);
  while (1)
  {
    if((m-n) >= 0) break;
    else m *= 10;
  }
  if(n == m) printf("%d의 자리수이다.", m);
  else printf("%d의 자리수이다.", m/10);
  return 0;
}
#include <stdio.h>
int main(void)
{
  double a;
  double *p = &a;
  scanf("%lf", p);
  printf("%.2lf", *p / 2);
}

#include <stdio.h>
int main(void)
{
  int num1, num2, i, lcm=0;
  scanf("%d %d", &num1, &num2);

  for (i = num1*num2; i >= 1; i--){
    if(i%num1==0 && i%num2==0) lcm = i;
  }
  printf("%d", i);
  return 0;
}
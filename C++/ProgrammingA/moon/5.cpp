#include <stdio.h>
int main(void)
{
  int a, b;
  printf("두 수를 입력하세요.\n");
  scanf("%d %d", &a, &b);
  printf("a = %d, b = %d\n", a, b);

  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
  printf("a = %d, b = %d\n", a, b);

  return 0;
}
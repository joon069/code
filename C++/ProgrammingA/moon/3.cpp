#include <stdio.h>
int main(void)
{
  int a, n;
  printf("a와 n을 입력하세요.\n");
  scanf("%d %d", &a, &n);
  printf("%d", a << n);

  return 0;
}
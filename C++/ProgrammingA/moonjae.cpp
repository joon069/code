#include <stdio.h>
#include <math.h>

int main(void)
{
  int a, b, c;
  int D=0;
  printf("ax^2+bx+c의 근을 찾기 위한 a,b,c를 입력하세요.\n");
  scanf("%d %d %d", &a, &b, &c);
  D = b * b - (4 * a * c);
  printf("D = %d\n", D);
  if (D > 0)
  {
    printf("근은 두개입니다.\n");
    printf("x1 = %f\n", (-b + sqrt(D)) / (2 * a));
    printf("x2 = %f\n", (-b - sqrt(D)) / (2 * a));
  }
  else if (D == 0)
  {
    printf("근은 하나입니다.\n");
    printf("x = %f\n",( -b / (2 * a)));
  }
  if( D < 0)
    printf("근이 허수근입니다.\n");

  return 0;
}
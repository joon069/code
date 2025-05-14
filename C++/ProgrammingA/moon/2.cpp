#include <stdio.h>
int main(void)
{
  int math, english, science;
  printf("수학, 영어, 과학 점수를 입력하시오.\n");
  scanf("%d %d %d", &math, &english, &science);
  int sum = math + english + science;
  double avg = sum / 3.0;
  printf("평균: %.2f\n", avg);
  if(avg >= 90)
    printf("A\n");
  else if(avg >= 80)
    printf("B\n");
  else if(avg >= 70)
    printf("C\n");
  else if(avg >= 60)
    printf("D\n");
  else
    printf("F\n");
  return 0;
}
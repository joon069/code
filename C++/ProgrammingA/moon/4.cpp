#include <stdio.h>
int main(void)
{
  int a, b;
  int OP;
  printf("비트 연산을 수행합니다.\n");
  printf("비트 연산을 수행할 두 수를 입력하세요.\n");
  printf("(1, 또는 0을 입력하세요. 안그러면 강준영)\n");
  scanf("%d %d", &a, &b);
  printf("무슨 연산을 할지 선택하시오.\n(AND=1, OR=2, XAND=3, NOR=4, XOR=5, XNOR=6): ");
  scanf("%d", &OP);
  switch(OP)
  {
    case 1:
      printf("AND 연산 결과: %d\n", a & b);
      break;
    case 2:
      printf("OR 연산 결과: %d\n", a | b);
      break;
    case 3:
      printf("XAND 연산 결과: %d\n", a ^ b);
      break;
    case 4:
      printf("NOR 연산 결과: %d\n", ~(a | b));
      break;
    case 5:
      printf("XOR 연산 결과: %d\n", a ^ b);
      break;
    case 6:
      printf("XNOR 연산 결과: %d\n", ~(a ^ b));
      break;
    default:
      printf("잘못된 선택입니다.\n");
  }

  return 0;
}
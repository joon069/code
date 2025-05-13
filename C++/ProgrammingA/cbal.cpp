#include <stdio.h>
/*int main(void)
{
  printf("\t\t\t강준영의 하루이야기.\n\n");
  printf("\t\t\"아침 6시 50분에 일어나 머리를 감은 후\"\n");
  printf("\t\"7시 10분에 기숙사를 나서서 학교에서 하루 계획을 세운다.\"\n\n");
  printf("\t\t\t\"수학 선생님꼐 혼나고\"\n");
  printf("\t\"학교에서 수업을 듣고 점심을 먹고 오후 4시에 수업이 끝난다.\"\n\n");

  printf("\t\t\t\"이시은에게 괴롭힘을 당한 후\"\n");
  printf("\t\t\t\"남은 방과후도 잘 보낸 후\"\n");
  printf("\t\"8시 45분, 기숙사로 돌아와 과제를 하거나 정신 못차리고 쉰다.\"\n");
  printf("\t\t\t\"그렇게 12에서 1시 쯤 잠에 든다.\"\n");
  printf("\t\t\t*\\강준영의 하루 끝\\*\n");
}*/
/*int main(void)
{
  int a, b;
  scanf("%d %d", &a, &b);
  printf("a = %d, b = %d\n", a, b);

  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
  printf("a = %d, b = %d\n", a, b);

  return 0;
}*/

/*int main(void)
{
  int a, n;
  scanf("%d %d", &a, &n);
  printf("%d", a << n);

  return 0;
}*/

/*int main(void)
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
}*/

/*int main(void)
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
}*/
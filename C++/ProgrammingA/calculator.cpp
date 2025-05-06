#include <stdio.h>
int main(void)
{
  char buho;
  int a, b;
  printf("x (+, -, *, /, %%) y 이런 형식으로 작성\n");
  scanf("%d %c %d", &a, &buho, &b);
  switch(buho)
  
  {
    case '+':
      printf("%d", a + b);
      break;
    
    case '-':
      printf("%d", a-b);
      break;

    case '*':
      printf("%d", a * b);
      break;

    case '/':
      printf("%f", (float)a / b);
      break;
    
    default:
      printf("이상한거 넣지마");
    }
}

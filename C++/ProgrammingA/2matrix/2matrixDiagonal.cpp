#include <stdio.h>
int main(void)
{
  int matrix[3][3];
  
  for (int i = 0; i < 3; i++){
    for (int j = 0; j < 3; j++){
      scanf("%d", &matrix[j][i]);
    }
  }
  //왼쪽 위에서 오른쪽 아래 합
  int sum = 0;
  sum = matrix[0][0] + matrix[1][1] + matrix[2][2];
  printf("%d\n", sum);

  sum = 0;
  sum = matrix[0][2] + matrix[1][1] + matrix[2][0];
  printf("%d", sum);
}
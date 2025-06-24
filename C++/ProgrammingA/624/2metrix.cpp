#include <stdio.h>
int main(void)
{
  int n, sum=0;
  scanf("%d", &n);
  int metrix[n][n];
  int i,j;
  for (i = 0; i < n; i++){
    for (j = 0; j < n; j++){
      scanf("%d", &metrix[i][j]);
    }
  }
  //왼쪽 대각선
  for (i = 0; i < n;i++){
    sum += metrix[i][i];
  }
  printf("%d", sum);

  //오른쪽 대각선 근데 이건 안해도 된데 이런.
  // sum = 0;
  // for (i = 0; i < n; i++)
  // {
  //   sum += metrix[i][n - i - 1];
  // }
  // printf("%d", sum);

  return 0;
}
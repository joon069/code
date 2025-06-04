#include <stdio.h>
int main(void)
{
  char roomA[100]={0};
  char roomB[100]={0};

  scanf("%s", roomB);

  for (int i = 0; roomB[i] != '\0';i++){
    roomA[i] = roomB[i];
  }
  printf("%s\n  ", roomA);

  return 0;
}
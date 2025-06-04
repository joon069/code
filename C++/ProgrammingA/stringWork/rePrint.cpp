#include <stdio.h>
int main(void)
{
  char room[100];
  scanf("%s", room);
  int len = 0;
  for (int i = 0; room[i] != '\0'; i++)
  {
    len += 1;
  }
  len -= 1;

  for (int i = len; room[i] >= 0; i--){
    printf("%c", room[i]);
  }

  return 0;
}
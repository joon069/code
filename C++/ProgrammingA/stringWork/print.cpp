#include <stdio.h>
int main(void)
{
  char room[100];
  scanf("%s", room);

  for (int i = 0; room[i]!='\0'; i++){
    printf("%c", room[i]);
  }

  return 0;
}
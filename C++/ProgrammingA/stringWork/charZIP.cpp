#include <stdio.h>
int main(void)
//inpuu aaabbcc => output a3b3c2
{
  char str[100];
  scanf("%s", str);
  int i = 0;
  while (str[i] != '\0') {
    int count = 1;
    while (str[i] == str[i + 1]) {
      count++;
      i++;
    }
    printf("%c%d", str[i], count);
    i++;
  }
  printf("\n");
  return 0;
}
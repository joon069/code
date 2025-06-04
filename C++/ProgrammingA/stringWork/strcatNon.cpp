#include <stdio.h>
int len(char s[]){
  int len = 0;
  for (int i = 0; s[i] != '\0'; i++)
  {
    len += 1;
  }
  return len;

}
int main(void)
{
  char a[100], b[100];
  scanf("%s", a);
  scanf("%s", b);
  int j = len(a);

  for (int i = 0; b[i] != '\0'; i++){
    a[j+i] = b[i];
    if(a[j + i+1]=='\0'){
      a[j + i+1] = '\0';
    }
  }
  printf("%s", a);

  return 0;
}
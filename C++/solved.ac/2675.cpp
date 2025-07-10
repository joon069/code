#include <stdio.h>

int main()
{
  int n, nn;
  char str[21];
  scanf("%d", &n);
  for(int i=0; i<n; i++){
    scanf("%d %s", &nn, str);
    for(int j=0; str[j]!='\0'; j++){
      for(int k=0; k<nn; k++){
        printf("%c", str[j]);
      }
    }
    printf("\n");
  }
  return 0;
}
#include <stdio.h>
int AND(int a, int b);
int OR(int a, int b);
int NOT(int n);

int main()
{
  int a, b;
  scanf("%d %d\n", &a, &b);

  printf("%d\n", AND(a, b));
  printf("%d\n", OR(a, b));
  printf("%d\n", NOT(a));
  printf("%d\n", NOT(b));
  
  return 0;
}

int AND(int a, int b){
  return a && b;
}
int OR(int a, int b){
  return a || b;
}
int NOT(int n){
  return !n;
}
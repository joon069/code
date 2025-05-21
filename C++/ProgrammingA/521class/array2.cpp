#include <stdio.h>
int main(void)
{
  //최대, 최소
  int arr2[10];
  int max = -1, min=1;
  for(int i =0; i < 10; i++){
    scanf("%d", &arr2[i]);
    
    if(max < arr2[i]){
        max = arr2[i];
    }
  }

  for (int i=0; i<10; i++){
    if(min > arr2[i]){
        min = arr2[i];
    }
  }
  printf("최대: %d\n최소: %d ", max,min);

  return 0;
}
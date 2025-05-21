#include <stdio.h>
int main(void)
{
  int arr3[10];
    for(int i=0; i<10; i++){
      scanf("%d", &arr3[i]);
      
      if(arr3[i]%2!=0){
          printf("%d ", arr3[i]);
      }
    }
  return 0;
}
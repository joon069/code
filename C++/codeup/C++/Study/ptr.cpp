#include <stdio.h>

int main(){
    int num = 10;
    int* num_ptr = &num;
    int** num_ptr_ptr = &num_ptr;

    *num_ptr = 20;
    printf("num: %d\n", num);
}
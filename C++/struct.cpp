#include <stdio.h>

struct number{
    char name[10];
    int age;
    int number;
};

int main(){
    struct number n;
    printf("Enter name: ");
    scanf("%9s", n.name);
    printf("Enter age: ");
    scanf("%d", &n.age);
    printf("Enter number: ");
    scanf("%d", &n.number);

    printf("Name: %s, Age: %d, Number: %d\n", n.name, n.age, n.number);
}
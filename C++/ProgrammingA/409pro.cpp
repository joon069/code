#include <stdio.h>
int main(void)
{
    long long monney;
    int object;
    printf("전재산을 넣어주세요.\n");
    printf("재산 :");
    scanf("%lld", &monney);
    printf("현재 당신이 가지고 싶은 것을 입력하세요.\n");
    printf("1. 비둘기\n");
    printf("2. 집\n");
    printf("3. 자동차\n");
    printf("4. 돌\n");
    printf("5. 아이스크림\n");
    printf("6. 햄버거\n");
    printf("7. 국밥\n");
    printf("8. 컵라면\n");
    printf("9. 과자\n");
    printf("10. 나는 거지다.\n");
    scanf("%d", &object);

    if(monney >= 1000000000000000000 && 1 == object)
    {
        printf("잔금이 100000000000000000010000000000000000000원 이상입니다.\n");
        printf("그럼에도 비둘기는 살 수 없습니다.\n");
    }
    else if(monney >= 1000000000 && 2 == object)
    {
        printf("잔금이 1000000000원 이상입니다.\n");
        printf("무려 집를 살 수있습니다.\n");
    }
    else if(monney >= 1000000000 && 3 == object)
    {
        printf("잔금이 1000000000원 이상입니다.\n");
        printf("무려 자동차를 살 수있습니다.\n");
    }
    else if(monney >= 1000000000 && 4 == object)
    {
        printf("잔금이 1000000000원 이상입니다.\n");
        printf("무려 용연향을 살 수있습니다.\n");
    }
    else if(monney >= 1000000 && 5 == object)
    {
        printf("잔금이 100000원 이상입니다.\n");
        printf("무려 아이스크림을 사 먹을 수있습니다.\n");
    }
    else if(monney >= 50000 && 6 == object)
    {
        printf("잔금이 50000원 이상입니다.\n");
        printf("무려 햄버거를 사 먹을 수있습니다.\n");
    }
    else if(monney >= 10000 && 7 == object)
    {
        printf("잔금이 10000원 이상입니다.\n");
        printf("무려 국밥을 사 먹을 수있습니다.\n");
    }
    else if(monney >= 5000 && 8 == object)
    {
        printf("잔금이 5000원 이상입니다.\n");
        printf("무려 컵라면을 사 먹을 수있습니다.\n");
    }
    else if(monney >= 1000 && 9 == object)
    {
        printf("잔금이 1000원 이상입니다.\n");
        printf("무려 과자 한봉지(이상) 사 먹을 수있습니다.\n");
    }
    else if(monney <= 999 && 10 == object)
    {
        printf("잔금이 999원 이하입니다.\n");
        printf("당신은 이 세상에서 살 수없습니다.\n");
    }
    else
    {
        printf("돈이 부족함으로 당신은 가질 수 없습니다.\n");
    }
}
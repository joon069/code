#include <stdio.h>
#include <string.h>

int main(void)
{
    char poop[20];
    printf("똥이 마려운가? 예 | 아니오 :");
    scanf("%s", poop);

    if(strcmp(poop, "예") == 0){
        printf("변기 가는 중...\n");
        printf("변기에 앉았니? 예 | 아니오 :");
        scanf("%s", poop);

        if(strcmp(poop, "예") == 0){
            printf("똥을 싸고 있니? 예 | 아니오 :");
            scanf("%s", poop);

            if(strcmp(poop, "예") == 0){
                printf("똥을 다 쌌니? 예 | 아니오 :");
                scanf("%s", poop);

                if(strcmp(poop, "예") == 0){
                    printf("변기 물 내리기\n");
                }else{
                    printf("어 그래 더 싸라\n");
                }
            }
            else{
                printf("폰 보지 말랬지!\n");
            }
        }else{
            printf("노상방변!\n");
        }
    }
    else if(strcmp(poop, "아니오") == 0){
        printf("변비니?\n");
    }
}
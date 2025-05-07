#include <stdio.h>
#include <string.h> // strcmp 함수 사용을 위해 필요

int main(void) {
    char sentance[20]; // 입력 버퍼 크기를 늘림

    printf("라면을 끓이자\n");
    printf("라면에 물을 넣었니?\n 예 | 아니요\n");
    scanf("%s", sentance);

    if (strcmp(sentance, "예") == 0) {
        printf("스프를 넣었니?\n 예 | 아니요\n");
        scanf("%s", sentance);

        if (strcmp(sentance, "예") == 0) {
            printf("라면을 넣었니?\n 예 | 아니요\n");
            scanf("%s", sentance);

            if (strcmp(sentance, "예") == 0) {
                printf("라면을 끓이자\n");
                printf("라면을 다 먹었니?\n 예 | 아니요\n");
                scanf("%s", sentance);

                if (strcmp(sentance, "예") == 0) {
                    printf("설거지 안하냐?\n");
                } else {
                    printf("5분컷 해야 하는거 아님?\n");
                    printf("이-지\n");
                }
            } else {
                printf("라면을 넣어야지!\n");
            }
        } else {
            printf("맹물 마시게?\n");
        }
    } else if (strcmp(sentance, "아니요") == 0) {
        printf("뭐 다 태워 먹을거야?\n");
    } else {
        printf("잘못된 입력입니다.\n");
    }

    return 0;
}
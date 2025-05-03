#include <stdio.h>

int main(void)
{
    int maze[10][10];
    for(int i = 0; i <10; i++){
        for(int j = 0; j<10;j++){
            scanf("%d", &maze[i][j]);
        }
    }
    int x=1, y=1;
    while(1){
        if(maze[y][x]==2){
            maze[y][x]=9;
            break;
        }
        else if(maze[y][x]==0) maze[y][x]=9;
        if(maze[y][x+1]==0){
            maze[y][x+1]=9;
            x++;
        }
        else if(maze[y][x+1]==1){
            if(maze[y+1][x]==1) break;
            else if(maze[y+1][x]==2){
                maze[y+1][x]=9;
                y++;
                break;
            }
            else if(maze[y+1][x]==0){
                maze[y+1][x]=9;
                y++;
            }
        }
        else if(maze[y][x+1]==2){
            maze[y][x+1]=9;
            x++;
            break;
        }
        if(x==8 && y==8) break;
    }
    for(int i = 0; i <10; i++){
        for(int j = 0; j<10;j++){
            printf("%d ",maze[i][j]);
        }
        printf("\n");
    }
    
    
    return 0;
}
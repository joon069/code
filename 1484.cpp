#include <stdio.h>
int main(void)
{   
    int dy[4] = {0, 1, 0, -1};
    int dx[4] = {1, 0, -1, 0};
    int d=0;
    int x=0, y=0;
    int num = 1;
    int n,m;
    scanf("%d %d", &n, &m);
    int arr[101][101]={0,};
    for(int i=1; i<=n*m; i++) {
        if(x + dx[d] < 0 ||
            x + dx[d] >= m || y + dy[d] < 0 || y+dy[d] >= n || arr[y+dy[d]][x+dx[d]] != 0){
            d = (d+1)%4;
        }
        arr[y][x] = i;
        x += dx[d];
        y += dy[d];
        
    }
    
    for(int i=0; i<n;i++){
        for(int j=0;j<m;j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}
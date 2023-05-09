#include <stdio.h>

int main()
{
    int N, M, A[100][100], B;
    scanf("%d %d", &N, &M);
    
    for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) scanf("%d", &A[i][j]);
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d", &B);
        
            printf("%d ", A[i][j] + B);
        }
        
        printf("\n");
    }
}
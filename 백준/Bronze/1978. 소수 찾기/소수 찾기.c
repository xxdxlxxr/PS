#include <stdio.h>

int main()
{
    int N, num, answer = 0;
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &num);
        
        for (int j = 2; j <= num; j++) {
            if (num == j) answer++;
            
            if (num % j == 0) break;
        }
    }
    
    printf("%d", answer);
}
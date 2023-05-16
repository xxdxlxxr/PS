#include <stdio.h>

int main()
{
    int M, N, sum = 0, minimum = 0;
    scanf("%d\n%d", &M, &N);
    
    for (int i = M; i <= N; i++) {
        for (int j = 2; j <= i; j++) {
            if (i % j == 0) break;
            
            if (j == i - 1) {
                if (sum == 0) minimum = i;
                
                sum += i;
            }
        }
        
        if (i == 2) {
            sum += i;
            minimum = i;
        }
    }
    
    if (minimum == 0) printf("-1");
    else printf("%d\n%d", sum, minimum);
}
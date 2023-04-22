#include <stdio.h>

int main()
{
    int N, score, max = 0;
    int sum = 0;
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d", &score);
        sum += score;
        
        if (score > max) max = score;
    }
    
    printf("%f", 100.0 * sum / max / N);
}
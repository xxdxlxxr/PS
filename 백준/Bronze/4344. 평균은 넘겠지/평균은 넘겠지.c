#include <stdio.h>

int main()
{
    int C, N;
    scanf("%d", &C);
    
    while (C--) {
        scanf("%d", &N);
        int scores[N], sum = 0, cnt = 0;
        double avg = 0;
        
        for (int i = 0; i < N; i++) {
            scanf("%d", scores + i);
            
            sum += scores[i];
        }
        
        avg = (double) sum / N;
        
        for (int i = 0; i < N; i++) if (scores[i] > avg) cnt++;
        
        printf("%.3lf%%\n", (double) 100 * cnt / N);
    }
}
#include <stdio.h>

int main()
{
    int N, min, max, tmp;
    scanf("%d", &N);
    scanf("%d", &min);
    max = min;
    
    for (int i = 1; i < N; i++) {
        scanf("%d", &tmp);
        
        if (max < tmp) max = tmp;
        if (min > tmp) min = tmp;
    }
    
    printf("%d %d", min, max);
}
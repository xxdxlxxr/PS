#include <stdio.h>

int main()
{
    int X, N, a, b;
    scanf("%d\n%d", &X, &N);
    
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &a, &b);
        
        X -= a * b;
    }
    
    if (X) printf("No");
    else printf("Yes");
}
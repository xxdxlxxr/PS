#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    
    while (N != 1) {
        for (int i = 2; i <= N; i++) {
            if (N % i == 0) {
                N /= i;
                printf("%d\n", i);
                break;
            }
        }
    }
}
#include <stdio.h>

int main()
{
    int N, answer = 1;
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) answer *= 2;
    
    printf("%d", (answer + 1) * (answer + 1));
}
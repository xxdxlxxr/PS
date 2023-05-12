#include <stdio.h>

int main()
{
    int N, tmp = 1, answer = 1;
    scanf("%d", &N);
    
    while (tmp < N) {
        tmp += 6 * answer;
        answer += 1;
    }
    
    printf("%d", answer);
}
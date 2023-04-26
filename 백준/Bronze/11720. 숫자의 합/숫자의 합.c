#include <stdio.h>

int main()
{
    int N, answer = 0;
    scanf("%d", &N);
    char nums[N];
    scanf("%s", nums);
    
    for (int i = 0; i < N; i++) answer += nums[i] - '0';
    
    printf("%d", answer);
}
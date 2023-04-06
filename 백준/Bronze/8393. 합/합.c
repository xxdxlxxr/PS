#include <stdio.h>

int main()
{
    int n, answer = 0;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) answer += i + 1;
    
    printf("%d", answer);
}
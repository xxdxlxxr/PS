#include <stdio.h>

int main()
{
    int X, i = 1, sum = 0;
    scanf("%d", &X);
    
    while (X > sum) {
        sum += i;
        i += 1;
    }
    
    if (i % 2) printf("%d/%d", X - sum + i - 1, sum - X + 1);
    else printf("%d/%d", sum - X + 1, X - sum + i - 1);
}
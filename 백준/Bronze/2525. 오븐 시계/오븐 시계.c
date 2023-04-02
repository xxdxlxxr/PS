#include <stdio.h>

int main()
{
    int A, B, C, temp;
    scanf("%d %d\n%d", &A, &B, &C);
    B += C;
    
    if (B >= 60) {
        temp = B / 60;
        A += temp;
        B %= 60;
        
        if (A >= 24) A %= 24;
    }
    
    printf("%d %d", A, B);
}
#include <stdio.h>

int main()
{
    int A, B;
    scanf("%d %d", &A, &B);
    
    A = A / 100 + ((A / 10) % 10) * 10 + ((A % 100) % 10) * 100;
    B = B / 100 + ((B / 10) % 10) * 10 + ((B % 100) % 10) * 100;
    
    if (A > B) printf("%d", A);
    else printf("%d", B);
}
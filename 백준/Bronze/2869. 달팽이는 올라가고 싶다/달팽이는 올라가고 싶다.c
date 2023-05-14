#include <stdio.h>

int main()
{
    int A, B, V;
    scanf("%d %d %d", &A, &B, &V);
    
    if ((V - A) % (A - B) == 0) printf("%d", (V - A) / (A - B) + 1);
    else printf("%d", (V - A) / (A - B) + 2);
}
#include <stdio.h>

int main()
{
    int H, M;
    scanf("%d %d", &H, &M);
    
    M -= 45;
    
    if (M < 0) {
        H-= 1;
        M += 60;
    }
    
    if (H == -1) H = 23;
    
    printf("%d %d", H, M);
}
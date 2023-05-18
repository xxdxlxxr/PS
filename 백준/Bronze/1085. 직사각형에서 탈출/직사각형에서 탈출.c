#include <stdio.h>

int main()
{
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    int answer = x;
    
    if (answer > w - x) answer = w - x;
    if (answer > y) answer = y;
    if (answer > h - y) answer = h - y;
    
    printf("%d", answer);
}
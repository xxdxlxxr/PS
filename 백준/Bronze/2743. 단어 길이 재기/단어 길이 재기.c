#include <stdio.h>

int main()
{
    int len = 0;
    char str[100];
    scanf("%s", str);
    
    for (int i = 0; str[i]; i++) len += 1;
    
    printf("%d", len);
}
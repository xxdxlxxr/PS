#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int i = 0; i < T; i++) {
        char str[1000] = {'\0', };
        scanf("%s", str);
        
        printf("%c%c\n", str[0], str[strlen(str) - 1]);
    }
}
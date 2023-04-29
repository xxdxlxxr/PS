#include <stdio.h>
#include <string.h>

int main()
{
    char s[1000000];
    scanf("%[^\n]", s);
    int cnt = 0;
    int len = strlen(s);
    
    if (len == 1) {
        if (s[0] == ' ') {
            printf("0\n");
            return 0;
        }
    }
    
    for (int i = 1; i < len - 1; i++) if (s[i] == ' ') cnt++;
    
    printf("%d\n", cnt + 1);
}
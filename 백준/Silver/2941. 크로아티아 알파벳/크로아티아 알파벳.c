#include <stdio.h>
#include <string.h>

int main()
{
    char s[100];
    scanf("%s", &s);
    int sum = strlen(s);
    
    for (int i = 0; i < strlen(s); i++) {
        if ((s[i] == 'l' || s[i] == 'n') & s[i + 1] == 'j') sum--;
        if (s[i] == 'd' & s[i + 1] == 'z' & s[i + 2] == '=') sum--;
        if (s[i] == '=' || s[i] == '-') sum--;
    }
    
    printf("%d", sum);
}
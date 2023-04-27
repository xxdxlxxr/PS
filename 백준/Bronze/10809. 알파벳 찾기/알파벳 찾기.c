#include <stdio.h>

int main()
{
    char s[100] = {0};
    scanf("%s", &s);
    
    for (int i = 97; i < 123; i++) {
        int j = 0;
        
        while (s[j]) {
            if (s[j] == (char)i) break;
            
            j++;
        }
        
        if (s[j] == (char)i) printf("%d ", j);
        else printf("-1 ");
    }
}
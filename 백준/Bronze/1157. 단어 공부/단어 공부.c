#include <stdio.h>
#include <string.h>

int main()
{
    char s[1000000], answer;
    int arr[26], len, max = 0;
    scanf("%s", s);
    len = strlen(s);
    
    for (int i = 0; i < len; i++) {
        if (s[i] >= 'a') arr[s[i] - 'a']++;
        else arr[s[i] - 'A']++;
    }
    
    for (int i = 0; i < 26; i++) {
        if (arr[i] == max) answer = '?';
        else if (arr[i] > max) {
            max = arr[i];
            answer = 'A' + i;
        }
    }
    
    printf("%c", answer);
}
#include <stdio.h>
#include <string.h>

int main()
{
    int N;
    char word[100];
    scanf("%d", &N);
    int cnt = N;
    
    for (int i = 0; i < N; i++) {
        char first = '.';
        int arr[26] = {0};
        scanf("%s", word);
        
        for (int j = 0; word[j] != '\0'; j++) {
            if (first != word[j]) {
                first = word[j];
                arr[word[j] - 'a'] += 1;
            }
            
            if (arr[word[j] - 'a'] == 2) {
                cnt -= 1;
                break;
            }
        }
    }
    
    printf("%d", cnt);
}
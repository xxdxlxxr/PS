#include <stdio.h>

int main()
{
    char input[15];
    int cnt = 0;
    scanf("%s", &input);
    
    for (int i = 0; i < strlen(input); i++) {
        if (input[i] >= 65 & input[i] <= 67) cnt += 3;
        else if (input[i] >= 68 & input[i] <= 70) cnt += 4;
        else if (input[i] >= 71 & input[i] <= 73) cnt += 5;
        else if (input[i] >= 74 & input[i] <= 76) cnt += 6;
        else if (input[i] >= 77 & input[i] <= 79) cnt += 7;
        else if (input[i] >= 80 & input[i] <= 83) cnt += 8;
        else if (input[i] >= 84 & input[i] <= 86) cnt += 9;
        else cnt += 10;
    }
    
    printf("%d", cnt);
}
#include <stdio.h>

int main()
{
    int n, arr[10], answer = 0;
    
    for (int i = 0; i < 10; i++) {
        scanf("%d", &n);
        
        arr[i] = n % 42;
    }
    
    for (int i = 0; i < 10; i++) {
        int cnt = 0;
        
        for (int j = i + 1; j < 10; j++) {
            if (arr[i] == arr[j]) {
                cnt++;
                break;
            }
        }
        
        if (cnt == 0) answer++;
    }
    
    printf("%d", answer);
}
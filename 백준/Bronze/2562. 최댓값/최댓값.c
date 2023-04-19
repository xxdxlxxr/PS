#include <stdio.h>

int main()
{
    int max = 0;
    int n, index;
    
    for (int i = 0; i < 9; i++) {
        scanf("%d", &n);
        
        if (max < n) {
            max = n;
            index = i + 1;
        }
    }
    
    printf("%d\n%d", max, index);
}
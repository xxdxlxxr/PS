#include <stdio.h>

int main()
{
    int n, students[30] = {0};
    
    for (int i = 0; i < 28; i++) {
        scanf("%d", &n);
        
        students[n - 1]++;
    }
    
    for (int i = 0; i < 30; i++) if (students[i] == 0) printf("%d\n", i + 1);
}
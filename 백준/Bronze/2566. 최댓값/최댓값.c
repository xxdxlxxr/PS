#include <stdio.h>

int main()
{
    int nums[9][9], answer = 0;
    int row = 0;
    int col = 0;
    
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            scanf("%d", &nums[i][j]);
            
            if (nums[i][j] > answer) {
                answer = nums[i][j];
                row = i;
                col = j;
            }
        }
    }
    
    printf("%d\n%d %d", answer, row + 1, col + 1);
}
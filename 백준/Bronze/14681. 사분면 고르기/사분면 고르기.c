#include <stdio.h>

int main()
{
    int arr[2][2] = {
        {3, 2},
        {4, 1}
    };
    
    int x, y;
    scanf("%d\n%d", &x, &y);

    x = (x / abs(x) + 1) / 2;
    y = (y / abs(y) + 1) / 2;
    
    printf("%d", arr[x][y]);
}
#include <stdio.h>

int main()
{
    int year;
    scanf("%d", &year);
    
    printf("%d", !(year % 4) && year % 100 || !(year % 400));
}
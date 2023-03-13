#include <iostream>
#include <stack>
using namespace std;

int main()
{
    int k, tmp;
    stack<int> stack1;
    cin >> k;
    
    for (int i = 1; i <= k; i++)
    {
        cin >> tmp;
        
        if (tmp == 0)
        {
            stack1.pop();
        }
        else
        {
            stack1.push(tmp);
        }
    }
    
    int sum = 0;
    
    while (stack1.empty() == 0)
    {
        sum += stack1.top();
        stack1.pop();
    }
    
    cout << sum;
    
    return 0;
}
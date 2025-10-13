N = int(input())
print('short' if N >= -32768 and N <= 32767 else 'int' if N >= -2147483648 and N <= 2147483647 else 'long long')
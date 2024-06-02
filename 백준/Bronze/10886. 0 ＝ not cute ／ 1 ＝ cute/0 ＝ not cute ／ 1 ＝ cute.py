N = int(input())
print('Junhee is ', end='')
print('cute!' if 2 * sum(int(input()) for _ in range(N)) > N else 'not cute!')
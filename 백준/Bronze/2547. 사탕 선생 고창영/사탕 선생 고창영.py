for _ in range(int(input())):
    _, N = input(), int(input())
    print('NO' if sum(int(input()) for _ in range(N)) % N else 'YES')
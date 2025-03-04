N = int(input())
X, S = map(int, input().split())

for _ in range(N):
    c, p = map(int, input().split())

    if c <= X and p > S:
        print('YES')
        break
else:
    print('NO')
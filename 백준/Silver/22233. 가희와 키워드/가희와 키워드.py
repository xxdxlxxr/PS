N, M = map(int, input().split())
memo, answer = set(input() for _ in range(N)), []

for _ in range(M):
    memo -= set(list(input().split(',')))
    print(len(memo))
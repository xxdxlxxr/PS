N = int(input())
tmp = []

for _ in range(N):
    A, B = map(int, input().split())
    tmp.append(A - B)

tmp.sort()

print(tmp[N // 2] - tmp[N // 2 - 1] + 1 if N % 2 == 0 else 1)
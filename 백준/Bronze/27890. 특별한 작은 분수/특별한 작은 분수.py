x0, N = map(int, input().split())

for _ in range(N):
    x0 = (2 * x0)^6 if x0 % 2 else int(x0 / 2)^6

print(x0)
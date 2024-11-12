n, m, p = map(int, input().split())
answer = 0

for r in range(1, n + 1):
    for c in range(1, m + 1):
        if 2 * (r + c) >= p:
            answer += (n - r + 1) * (m - c + 1)

print(answer)
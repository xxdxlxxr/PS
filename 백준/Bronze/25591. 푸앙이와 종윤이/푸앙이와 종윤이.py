n, m = map(int, input().split())
a, b, c, d, q, r = 100 - n, 100 - m, n + m - 100, (n - 100) * (m - 100), (n - 100) * (m - 100) // 100, ((n - 100) * (m - 100)) % 100

print(a, b, c, d, q, r)
print(c + q, r)
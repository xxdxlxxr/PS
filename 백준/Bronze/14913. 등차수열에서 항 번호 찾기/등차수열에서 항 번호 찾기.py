a, d, k = map(int, input().split())
print('X' if (a < k) * (d < 0) or (a > k) * (d > 0) or (k - a) % d else (k - a) // d + 1)
m, n = int(input()), int(input())
print([2 * (m + n) - 4, m * n][min(m, n) < 3])
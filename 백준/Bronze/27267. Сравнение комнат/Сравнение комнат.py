a, b, c, d = map(int, input().split())
ab, cd = a * b, c * d
print('E' if ab == cd else 'M' if ab > cd else 'P')
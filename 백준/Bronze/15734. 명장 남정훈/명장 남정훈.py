L, R, A = map(int, input().split())

print(2 * min(L + A, R + A, L + R + A >> 1))
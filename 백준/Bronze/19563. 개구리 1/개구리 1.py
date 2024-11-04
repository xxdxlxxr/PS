a, b, c = map(int, input().split())
print('YES' if abs(a) + abs(b) <= c and (a + b) % 2 == c % 2 else 'NO')
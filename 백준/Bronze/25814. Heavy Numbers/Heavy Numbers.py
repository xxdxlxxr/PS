a, b = input().split()
a, b = len(a) * sum(map(int, a)), len(b) * sum(map(int, b))

print(0 if a == b else (a < b) + 1)
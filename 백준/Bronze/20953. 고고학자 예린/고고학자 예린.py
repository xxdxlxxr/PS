import sys

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print((a + b - 1) * (a + b) ** 2 // 2)
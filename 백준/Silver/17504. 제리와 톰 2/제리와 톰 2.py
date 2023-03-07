N = int(input())
A = list(map(int, input().split()))
a, b = A[-1], A[-1] * A[-2] + 1

if N >= 3:
    for i in range(3, N + 1):
        a, b = b, b * A[-i] + a

print(b - a, b)
def check(x, a, b):
    return 0 < x % (a + b) < a + 1

A, B, C, D = map(int, input().split())

for m in map(int, input().split()):
    print(check(m, A, B) + check(m, C, D))
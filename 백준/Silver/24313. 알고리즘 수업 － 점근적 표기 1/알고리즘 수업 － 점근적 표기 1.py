a1, a0 = map(int, input().split())
c, n0 = int(input()), int(input())
print(int(c >= a1 and a1 * n0 + a0 <= c * n0))
W, N, P = map(int, input().split())
print(sum(W <= h <= N for h in map(int, input().split())))
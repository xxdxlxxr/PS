N, K = map(int, input().split())
print("NO" if sum((A + 1) // 2 for A in map(int, input().split())) < N else "YES")
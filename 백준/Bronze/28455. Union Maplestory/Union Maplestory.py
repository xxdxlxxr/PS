N = int(input())
union = sorted([int(input()) for _ in range(N)], reverse=True)[:min(42, N)]
print(sum(union), sum(5 if L >= 250 else 4 if L >= 200 else 3 if L >= 140 else 2 if L >= 100 else 1 if L >= 60 else 0 for L in union))
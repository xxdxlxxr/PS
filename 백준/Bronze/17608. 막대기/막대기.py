height = [int(input()) for _ in range(int(input()))]
cur, cnt = height[-1], 1

for h in reversed(height[:-1]):
    if h > cur:
        cur = h
        cnt += 1

print(cnt)
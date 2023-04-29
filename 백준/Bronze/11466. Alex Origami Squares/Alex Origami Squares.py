h, w = map(int, input().split())

print(max(max(h, w) / 3 if max(h, w) / 3 <= min(h, w) else min(h, w), min(h, w) / 2))
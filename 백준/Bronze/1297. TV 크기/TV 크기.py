D, H, W = map(int, input().split())
tmp = D / (H ** 2 + W ** 2) ** .5
print(int(tmp * H), int(tmp * W))
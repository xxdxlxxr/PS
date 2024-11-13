H, W, N, M = map(int, input().split())
print((H // (N + 1) + (H % (N + 1) != 0)) * (W // (M + 1) + (W % (M + 1) != 0)))
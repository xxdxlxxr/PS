N, T = int(input()), sum(map(int, input().split()))

print((8 * (N - 1) + T) // 24, (8 * (N - 1) + T) % 24)
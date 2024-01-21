N, a = int(input()), list(map(int, input().split()))

print(max(a[i] - N + i for i in range(N)))
n, x = int(input()), list(map(int, input().split()))

print(2 * sum(abs(x[i] - x[j]) for i in range(n) for j in range(i, n)))
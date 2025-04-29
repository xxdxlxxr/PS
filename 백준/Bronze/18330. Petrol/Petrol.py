n, k = int(input()), int(input())
x = min(k + 60, n)
print(1500 * x + 3000 * (n - x))
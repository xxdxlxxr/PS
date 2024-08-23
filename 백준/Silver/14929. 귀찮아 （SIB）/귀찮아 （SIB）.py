n, x, cum = int(input()), list(map(int, input().split())), [0]

for i in range(n):
    cum.append(x[i] + cum[i])

cum.pop(0)
print(sum(x[i] * (cum[-1] - cum[i]) for i in range(n - 1)))
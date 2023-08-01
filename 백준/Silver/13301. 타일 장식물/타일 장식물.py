N, arr = int(input()), [1, 1]

for i in range(N - 1):
    arr.append(arr[-2] + arr[-1])

print(2 * (arr[-2] + arr[-1]))
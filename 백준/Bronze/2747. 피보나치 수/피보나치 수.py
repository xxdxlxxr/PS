arr = [0, 1]

for _ in range(int(input()) - 1):
    arr.append(arr[-2] + arr[-1])

print(arr[-1])
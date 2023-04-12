N, arr = int(input()), []

for _ in range(N):
    title, diff = input().split()

    arr.append([diff, title])

print(sorted(arr)[0][1])
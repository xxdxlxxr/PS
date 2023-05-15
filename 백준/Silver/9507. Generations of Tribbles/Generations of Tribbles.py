arr = [1, 1, 2, 4]

for _ in range(64):
    arr.append(sum(arr[-4:]))

for _ in range(int(input())):
    print(arr[int(input())])
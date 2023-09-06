arr = list(map(int, input().split()))

while arr != list(range(1, 6)):
    for i in range(4):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)
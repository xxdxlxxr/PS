n, arr = int(input()), list(map(int, input().split()))

for _ in range(int(input())):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number - 1, n, number):
            arr[i] = int(not arr[i])
    else:
        arr[number - 1] = int(not arr[number - 1])

        for i in range(min(number - 1, n - number)):
            if arr[number - i - 2] == arr[number + i]:
                arr[number - i - 2] = int(not arr[number - i - 2])
                arr[number + i] = int(not arr[number + i])
            else:
                break

for i in range(0, n, 20):
    print(*arr[i:i + 20])
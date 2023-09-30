for _ in range(int(input())):
    n = int(input())
    arr = n * [1]

    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            arr[j - 1] = not(arr[j - 1])

    print(sum(arr))
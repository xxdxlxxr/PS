for _ in range(int(input())):
    arr = [int(input())]

    while arr[-1] != 1:
        arr.append(3 * arr[-1] + 1 if arr[-1] % 2 else arr[-1] // 2)

    print(max(arr))
while 1:
    Hour, arr = int(input()), [1, 1]

    if Hour == -1:
        break

    for _ in range(Hour - 2):
        arr.append(arr[-2] + arr[-1])

    print(f'Hour {Hour}: {arr[-1]} cow(s) affected')
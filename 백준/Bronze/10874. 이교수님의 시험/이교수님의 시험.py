for i in range(int(input())):
    if list(map(int, input().split())) == 2 * list(range(1, 6)):
        print(i + 1)
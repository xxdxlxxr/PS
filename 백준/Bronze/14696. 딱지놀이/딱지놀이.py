for _ in range(int(input())):
    a, b = list(map(int, input().split()))[1:], list(map(int, input().split()))[1:]

    for i in range(4, 0, -1):
        if a.count(i) > b.count(i):
            print('A')
            break
        elif a.count(i) < b.count(i):
            print('B')
            break

        if i == 1:
            print('D')
for _ in range(int(input())):
    x, y = input().split()

    print('Distances: ', end='')
    print(*(ord(y[i]) - ord(x[i]) if y[i] >= x[i] else ord(y[i]) - ord(x[i]) + 26 for i in range(len(x))))
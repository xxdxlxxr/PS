for _ in range(int(input())):
    a, b = map(int, input().split())

    for char in input():
        print(chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A')), end='')

    print()
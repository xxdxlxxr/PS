for _ in range(int(input())):
    R, S = input().split()

    for char in S:
        print(int(R) * char, end = '')

    print()
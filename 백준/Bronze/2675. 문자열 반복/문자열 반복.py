for _ in range(int(input())):
    S, R = input().split()

    for char in R:
        print(int(S) * char, end = '')

    print()
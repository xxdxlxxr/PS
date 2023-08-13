for _ in range(int(input())):
    sides1, sides2, folds = map(int, input().split())

    print('Data set:', sides1, sides2, folds)

    for _ in range(folds):
        if sides1 < sides2:
            sides1, sides2 = sides2, sides1

        sides1 = int(sides1 / 2)

    print(max(sides1, sides2), min(sides1, sides2))
    print()
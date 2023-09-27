for i in range(int(input())):
    h, cb = int(input()), input()

    print(f'Data Set {i + 1}:')
    print(h - cb.count('b') + cb.count('c'))
    print()
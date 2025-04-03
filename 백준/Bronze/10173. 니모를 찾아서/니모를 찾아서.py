while 1:
    S = input()

    if S == 'EOI':
        break

    print(['Missing', 'Found']['nemo' in S.lower()])
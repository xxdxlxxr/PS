for _ in range(int(input())):
    a, b = input(), input()
    print(f'Hamming distance is {sum(a[i] != b[i] for i in range(len(a)))}.')
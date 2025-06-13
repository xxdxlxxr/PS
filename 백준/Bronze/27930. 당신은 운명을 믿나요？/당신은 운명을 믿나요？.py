y, k = list('YONSEI'), list('KOREA')

for char in input():
    if char == k[0]:
        k.remove(char)

        if len(k) == 0:
            print("KOREA")
            break

    if char == y[0]:
        y.remove(char)

        if len(y) == 0:
            print("YONSEI")
            break
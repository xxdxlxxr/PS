R, C, ZR, ZC = map(int, input().split())

for _ in range(R):
    article = input()

    for _ in range(ZR):
        print(''.join(ZC * char for char in article))
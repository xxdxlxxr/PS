h = int(input())

if h <= 1:
    print(int(not h))
else:
    print((h % 2) * '4' + (h // 2) * '8')
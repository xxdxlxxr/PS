A, P = map(int, input().split())
tmp = [A]

while 1:
    num = 0

    for i in str(tmp[-1]):
        num += (int(i) ** P)

    if num in tmp:
        break

    tmp.append(num)

print(tmp.index(num))
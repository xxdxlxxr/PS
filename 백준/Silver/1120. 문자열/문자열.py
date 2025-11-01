a, b = input().split()
tmp = []

for i in range(len(b) - len(a) + 1):
    cnt = 0

    for j in range(len(a)):
        if a[j] != b[i + j]:
            cnt += 1

    tmp.append(cnt)

print(min(tmp))
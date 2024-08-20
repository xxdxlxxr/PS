N, cnt, answer = int(input()), list(map(int, input().split())), -1

for i in range(N + 1):
    tmp = cnt.count(i)

    if tmp == i:
        answer = i

print(answer)
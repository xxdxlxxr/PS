from collections import deque

N, tmp = int(input()), deque()

while 1:
    num = int(input())

    if num == -1:
        break

    if num == 0:
        tmp.popleft()
    elif len(tmp) < N:
        tmp.append(num)

print(*tmp if tmp else 'empty')
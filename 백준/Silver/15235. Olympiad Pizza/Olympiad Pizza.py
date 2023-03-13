import sys
from collections import deque

N = int(sys.stdin.readline())
pizza = list(map(int, sys.stdin.readline().split()))
answer = [0 for i in range(N)]
queue = deque()

for i in range(N):
    queue.append([i, 0])

cnt = 0

while queue:
    num, get = queue.popleft()
    cnt += 1
    get += 1

    if pizza[num] == get:
        answer[num] = cnt
    else:
        queue.append([num, get])

print(*answer)
from collections import deque

N, q, answer = int(input()), deque(enumerate(map(int, input().split()))), []

while q:
    i, paper = q.popleft()
    answer.append(i + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(*answer)
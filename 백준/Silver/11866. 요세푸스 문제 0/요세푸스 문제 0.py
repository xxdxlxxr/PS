from collections import deque

N, K = map(int, input().split())
queue, answer = deque([i + 1 for i in range(N)]), []

for i in range(N):
    queue.rotate(-(K - 1))
    answer.append(str(queue.popleft()))

print('<' + ', '.join(answer) + '>', end = '')
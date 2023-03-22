from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        maximum = max(queue)
        first = queue.popleft()
        M -= 1

        if first == maximum:
            cnt += 1

            if M < 0:
                print(cnt)
                break
        else:
            queue.append(first)

            if M < 0:
                M = len(queue) - 1
from collections import deque

initials = deque([list(input().split()) for _ in range(int(input()))])

while len(initials) > 1:
    init, num = initials.popleft()

    for _ in range(int(num) - 1):
        initials.append(initials.popleft())

    initials.popleft()

print(initials[0][0])
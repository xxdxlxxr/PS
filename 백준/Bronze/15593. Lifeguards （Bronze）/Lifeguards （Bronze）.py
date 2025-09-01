lifeguards, work, answer = 1000 * [0], [], 0

for _ in range(int(input())):
    start, end = map(int, input().split())
    work.append((start, end))

    for i in range(start, end):
        lifeguards[i] += 1

for w in work:
    time, start, end = 0, w[0], w[1]

    for i in range(start, end):
        lifeguards[i] -= 1

    for lifeguard in lifeguards:
        if lifeguard > 0:
            time += 1

    answer = max(time, answer)

    for i in range(start, end):
        lifeguards[i] += 1

print(answer)
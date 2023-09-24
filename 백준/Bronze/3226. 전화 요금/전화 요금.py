answer = 0

for _ in range(int(input())):
    start, DD = input().split()
    start = list(map(int, start.split(':')))
    end, DD = start.copy(), int(DD)
    end[1] += DD
    answer += DD

    if end[1] >= 60:
        end[0] += 1
        end[1] -= 60

        if end[0] == 24:
            end[0] = 0

    if 6 < start[0] < 19:
        answer += 60 - start[1] if end[0] == 19 else DD
    elif end[0] == 7:
        answer += end[1]

print(5 * answer)
N, target, answer = int(input()), list(input()), 0

for _ in range(N - 1):
    compare, cnt = target[:], 0

    for w in input():
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
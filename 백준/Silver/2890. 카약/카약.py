R, C = map(int, input().split())
score = 10 * [0]

for _ in range(R):
    line, i = input(), 1

    while i + 1 < C:
        if line[i].isnumeric():
            score[int(line[i])] = i
            i += 2

        i += 1

sorted_score = sorted(set(score[1:]), reverse=True)

for rank in (sorted_score.index(num) + 1 for num in score[1:]):
    print(rank)
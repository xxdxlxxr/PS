score, max_score, hacker = list(map(int, input().split())), [i // 2 + 1 for i in range(9)], 0

for i in range(9):
    if score[i] > 100 * max_score[i]:
        hacker = 1
        break

print('hacker' if hacker else 'draw' if sum(score) > 99 else 'none')
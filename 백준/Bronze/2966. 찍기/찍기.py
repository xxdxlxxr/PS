N, sol, pattern, score = int(input()), input(), ['ABC', 'BABC', 'CCAABB'], 3 * [0]

for i in range(N):
    for j in range(3):
        if pattern[j][i % len(pattern[j])] == sol[i]:
            score[j] += 1

m = max(score)
print(m)

for i in range(3):
    if score[i] == m:
        print(['Adrian', 'Bruno', 'Goran'][i])